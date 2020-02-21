import datetime
import codecs
import getopt
import sys

import requests
import os
import time

from wordcloud import WordCloud
import jieba



# Used to store today's repos' descriptions
CONTENT = []









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
    opts, args = getopt.getopt(sys.argv[1:], "g:")
    git_switch = True
    for op, value in opts:
        if op == "-g" and value == "off":
            git_switch = False

    while True:
        main(git_switch)

        # Crawl the GitHub trending pages once a day
        time.sleep(24 * 60 * 60)
