import logging

import requests
from pyquery import PyQuery as pq

from repository_info import RepoInfo


class GitHubCrawler:
    """
    GitHub trending crawler
    """

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }

    TRENDING_URL = 'https://github.com/trending/{language}?since={frequency}'
    # frequency of trending
    FREQUENCY = ['daily', 'weekly', 'monthly']
    # programming languages you are interested in
    LANGUAGES = ['python', 'java', 'unknown', 'javascript', 'html', 'go']

    def __init__(self):
        self.content = []
        self.logger = logging.getLogger('main')

    @staticmethod
    def __parse(dollar):
        """
        Parse and extract useful information from html by pyquery.

        :param dollar: the pyquery object, just like $ in jquery
        :return: a list includes many `RepoInfo` objects
        """
        repo_infos = []

        articles = dollar('.explore-pjax-container.container-lg.p-responsive.pt-6 > div > div:nth-child(2)').children()
        for i in range(len(articles)):
            article = articles.eq(i)

            # href: '/Username/RepoName'
            href = article('.lh-condensed a').attr('href')

            # the description about the repo
            desc = article('.col-9.text-gray.my-1.pr-4').text().strip().replace('\n', '')

            # how many stars it got
            stars = article('div.f6.text-gray.mt-2 > span.d-inline-block.float-sm-right').text().strip()

            repo_infos.append(RepoInfo(href=href, stars=stars, desc=desc))

        return repo_infos

    def crawl(self, lang):
        ret = []
        try:
            url = self.TRENDING_URL.format(language=lang)
            r = requests.get(url, headers=self.HEADERS)

            # If the status code is not 200, then raise the error
            r.raise_for_status()

            # Use pyquery to parse html
            infos = self.__parse(pq(r.text))
            append_text_to_md(filename, language, info)

        except Exception as e:
            self.logger.exception(e)
        else:
            self.logger.info('Done: %s', lang)

def crawl(language, filename):
    """
    Crawling the GitHub trending page of the language.

    :param language: the page of the language you want to get.
    :param filename: the markdown file's name
    """
