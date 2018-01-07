import datetime
import codecs
import requests
import os
import time
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

CLASS = ['col-12', 'd-block', 'width-full', 'py-4', 'border-bottom']

objectives = ['python', 'java', 'unknown', 'c++', 'html']


# Upload file by git
def git_add_commit_push(date, filename):
    cmd_git_add = 'git add {filename}'.format(filename=filename)
    cmd_git_commit = 'sudo git commit -m "{date}"'.format(date=date)
    cmd_git_push = 'sudo git push -u origin master'

    os.system(cmd_git_add)
    os.system(cmd_git_commit)
    os.system(cmd_git_push)


# Create markdown file to save trending repos
def create_markdown(date, filename):
    with open(filename, 'w') as f:
        f.write("## " + date + "\n")


def crawl(language, filename):
    try:
        url = 'https://github.com/trending/{language}'.format(language=language)
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")

        # codecs to solve the problem utf-8 codec like Chinese
        with codecs.open(filename, "a", "utf-8") as f:
            f.write('\n### {language}\n'.format(language=language))
            for li in soup.find_all('li'):
                if li.attrs.get('class') == CLASS:
                    description = ''
                    url = "https://github.com"
                    if li.p:
                        for s in li.p.contents:
                            description += str(s).strip()
                    postfix = li.h3.a.attrs['href']
                    url += postfix
                    # owner = postfix.spilt('/')[1]
                    # title = postfix.spilt('/')[2]
                    f.write(u"* [{title}]({url}): {description}\n".format(title=postfix[1:], url=url,
                                                                          description=description))
        print("Finish crawling: " + language)

    except requests.ConnectionError:
        print("Connection Error.")
    except IOError:
        print("IOError.")


def job():
    strdate = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = '{date}.md'.format(date=strdate)

    # create markdown file
    create_markdown(strdate, filename)

    for obj in objectives:
        try:
            crawl(obj, filename)
        except:
            print("Error: " + obj)
            time.sleep(5)
            continue
    print("Finish crawling: " + strdate)

    # Upload results
    git_add_commit_push(strdate, filename)


if __name__ == '__main__':
    while True:
        job()

        # Crawling the repos every day
        time.sleep(24 * 60 * 60)
