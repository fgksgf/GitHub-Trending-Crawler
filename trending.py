import datetime
import codecs
import getopt
import sys

import requests
import os
import time
from pyquery import PyQuery as pq
from wordcloud import WordCloud
import jieba

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

# Programming languages you are interested in
# See https://github.com/trending for more available languages
LANGUAGES = ['python', 'java', 'unknown', 'javascript', 'html', 'go']

TRENDING_URL = 'https://github.com/trending/{language}'
GITHUB_URL = 'https://github.com'

# Used to store today's repos' descriptions
CONTENT = []


def git_add_commit_push(date, filename):
    """
    Upload the markdown file and the image to GitHub by git. 
    
    :param date: today's date.
    :param filename: the markdown file's name.
    """
    cmd_git_pull = 'git pull'
    cmd_git_add_md = 'git add {filename}'.format(filename=filename)
    cmd_git_add_img = 'git add img/{date}.png'.format(date=date)
    cmd_git_commit = 'git commit -m "{date}"'.format(date=date)
    cmd_git_push = 'git push -u origin master'

    os.system(cmd_git_pull)
    os.system(cmd_git_add_md)
    os.system(cmd_git_add_img)
    os.system(cmd_git_commit)
    os.system(cmd_git_push)


def create_markdown(date, filename):
    """ 
    Create a markdown file to save trending repos.
    
    :param date: today's date.
    :param filename: the markdown file's name.
    """
    with open(filename, 'w') as f:
        f.write("# " + date + "\n")
        f.write("See what the GitHub community is most excited about today.\n")


def generate_word_cloud(content_list, date):
    """
    Generate a word cloud picture according to all descriptions of today.
    Then save the picture at 'img/', which is named by date.
    
    :param content_list: a list contains all descriptions of today.
    :param date: today's date.
    """
    # Join all strings in the list with ''
    text = ''.join(content_list)

    # Use jieba to do Chinese word segmentation first
    word_list = jieba.cut(text, cut_all=False)
    f = " ".join(word_list)

    # Set the word cloud's attributes
    wc = WordCloud(background_color="white",
                   width=800,
                   height=600,
                   margin=2,
                   font_path='MSYH.TTC',  # Use this font to ensure Chinese words can be shown
                   random_state=20).generate(f)

    # Save the picture
    wc.to_file('img/{date}.png'.format(date=date))


def extract_info(dollar):
    """
    Extract useful information from html by pyquery, 
    which contains the repo's url, name, description
    and stars it got today.
    
    :param dollar: the pyquery object, just like $ in jquery 
    :return: a dict includes above information
    """
    names = []
    urls = []
    stars = []
    descriptions = []

    ol = dollar('.repo-list').children()
    for i in range(len(ol)):
        li = ol.eq(i)

        # postfix: '/Username/RepoName'
        postfix = li('div.d-inline-block.col-9.mb-1 > h3 > a').attr('href')

        # the complete url of the repo
        url = GITHUB_URL + postfix
        urls.append(url)

        p = postfix.rindex('/')
        # owner = postfix[:p]
        repo_name = postfix[p + 1:]
        names.append(repo_name)

        # Get the description about the repo
        description = li('.py-1').text().strip().replace('\n', '')
        descriptions.append(description)
        CONTENT.append(description)

        # Get how many stars it got today
        star = li('div.f6.text-gray.mt-2 > span.d-inline-block.float-sm-right').text().strip()
        stars.append(star)

    ret_dict = {'names': names, 'urls': urls, 'stars': stars, 'descriptions': descriptions}
    return ret_dict


def append_text_to_md(filename, language, info):
    """
    Append all repos' information of a language to the markdown file.
    
    :param filename: the markdown file's name
    :param language: the programming language
    :param info: a dict contains all repos' information
    """
    # Use codecs to solve the utf-8 encoding problem like Chinese
    with codecs.open(filename, "a", "utf-8") as f:
        f.write('\n## {language}\n'.format(language=language))
        for i in range(len(info['names'])):
            name = info['names'][i]
            url = info['urls'][i]
            star = info['stars'][i]
            desc = info['descriptions'][i]
            f.write(u"* [{name}]({url})(**{star}**): {desc}\n".format(name=name, url=url,
                                                                      desc=desc,
                                                                      star=star))


def append_img_to_md(filename, date):
    """
    Append an image of word cloud based on all descriptions
    to the markdown file.
    
    :param filename: the markdown file's name
    :param date: today's date, the image's name as well
    """
    img_path = 'img/{date}.png'.format(date=date)
    with codecs.open(filename, "a", "utf-8") as f:
        f.write('\n## WordCloud\n')
        f.write('![]({path})\n'.format(path=img_path))


def crawl(language, filename):
    """ 
    Crawling the GitHub trending page of the language.
    
    :param language: the page of the language you want to get.
    :param filename: the markdown file's name
    """
    try:
        url = TRENDING_URL.format(language=language)
        r = requests.get(url, headers=HEADERS)

        # If the status code is not 200, then raise the error
        r.raise_for_status()

        # Use pyquery to parse html
        d = pq(r.text)

        info = extract_info(d)
        append_text_to_md(filename, language, info)
        print("Done: " + language)
    except requests.ConnectionError:
        print("Connection Error.")
    except IOError:
        print("IOError.")


def main(git_switch=True):
    CONTENT.clear()

    # get today's date
    today_date = datetime.datetime.now().strftime('%Y-%m-%d')

    # The markdown file's name
    filename = '{date}.md'.format(date=today_date)

    # Create markdown file
    create_markdown(today_date, filename)

    for lang in LANGUAGES:
        try:
            crawl(lang, filename)
        except:
            print("Error: " + lang)
            time.sleep(2)
            continue

    generate_word_cloud(CONTENT, today_date)
    append_img_to_md(filename, today_date)
    print("Finish crawling: " + today_date)

    # Upload the markdown file to GitHub
    if git_switch:
        git_add_commit_push(today_date, filename)


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "g:l:")

    # whether use git push
    git_switch = True

    # whether use dead cycle
    loop = True

    for op, value in opts:
        if op == "-g" and value == "off":
            git_switch = False
        if op == "-l" and value == "off":
            loop = False
    while True:
        main(git_switch)

        # Crawl the GitHub trending pages once a day
        if loop:
            time.sleep(24 * 60 * 60)
        else:
            break
