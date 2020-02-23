"""GitHub Trending Crawler.

Usage:
  main.py (-h | --help)
  main.py (-v | --version)
  main.py [-l | --loop] [-p | --push] [--frequency=<f>]

Options:
  -h --help        Show this screen.
  -v --version     Show version.
  -l --loop        Run this program cyclically.
  -p --push        Use git to push the markdown and the image.
  --frequency=<f>  Speed in knots [default: daily].

"""
import time

from docopt import docopt

from config import DAY, LANGUAGES
from crawler import GitHubCrawler
from utils.git_util import git_add_commit_push

if __name__ == '__main__':
    arguments = docopt(__doc__, version='GitHub Trending Crawler V1.5')

    frequency = {'daily': DAY,
                 'weekly': 7 * DAY,
                 'monthly': 30 * DAY}

    f = arguments['--frequency']

    if f not in frequency.keys():
        print("The parameter --frequency should be 'daily', 'weekly' or 'monthly'.")
    else:
        crawler = GitHubCrawler(frequency=f)
        while True:
            crawler.run(langs=LANGUAGES)

            if arguments['--push']:
                git_add_commit_push()

            if arguments['--loop']:
                if f in frequency.keys():
                    time.sleep(frequency.get(f))
                else:
                    time.sleep(DAY)
            else:
                break
