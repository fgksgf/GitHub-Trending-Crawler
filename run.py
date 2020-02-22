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
