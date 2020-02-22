import datetime
import logging
import sys

import requests
from pyquery import PyQuery as pq

from config import TRENDING_URL, HEADERS, MD_FILE_NAME, LANGUAGES, FREQUENCY, PROXY_POOL_API
from repository_info import RepoInfo
from utils.file_util import append_infos_to_md, create_markdown, generate_wordcloud, append_img_to_md


class GitHubCrawler:
    """
    GitHub trending crawler
    """

    def __init__(self, frequency='daily', use_proxy=False):
        if frequency not in FREQUENCY:
            self.frequency = 'daily'
        else:
            self.frequency = frequency

        self.use_proxy = use_proxy

        # init logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)

        # output logs to console
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(level=logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%Y/%m/%d %H:%M:%S')
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def get_random_proxy(self):
        """
        Get a random proxy.

        :return: a proxy or None
        """
        proxies = {
            'http': '',
            'https': '',
        }
        try:
            response = requests.get(PROXY_POOL_API['get_a_proxy'])
            if response.status_code == 200:
                proxy = 'http://' + str(response.json()['proxy'])
                proxies['http'] = proxy
                proxies['https'] = proxy
        except Exception:
            self.logger.error('Failed to get a proxy!')
            return None
        else:
            return proxies

    def parse(self, dollar):
        """
        Parse and extract useful information from html by pyquery.
        If the trending page changes, just modify this method.

        :param dollar: the pyquery object, just like $ in jquery
        :return: a list includes many `RepoInfo` objects
        """
        repo_infos = []
        try:
            articles = dollar(
                '.explore-pjax-container.container-lg.p-responsive.pt-6 > div > div:nth-child(2)').children()
            for i in range(len(articles)):
                article = articles.eq(i)

                # href: '/Username/RepoName'
                href = article('.lh-condensed a').attr('href')

                # the description about the repo
                desc = article('.col-9.text-gray.my-1.pr-4').text().strip().replace('\n', '')

                # how many stars it got
                stars = article('div.f6.text-gray.mt-2 > span.d-inline-block.float-sm-right').text().strip()

                repo_infos.append(RepoInfo(href=href, stars=stars, desc=desc))
        except Exception:
            self.logger.error("The GitHub trending page changed, can't parse!")

        return repo_infos

    def crawl(self, lang):
        """
        Crawl a programming language trending page.

        :param lang: programming language name
        :return: a list includes many `RepoInfo` objects
        """
        ret = None
        try:
            url = TRENDING_URL.format(language=lang, frequency=self.frequency)

            proxies = None
            if self.use_proxy:
                proxies = self.get_random_proxy()
            if proxies:
                r = requests.get(url, headers=HEADERS, proxies=proxies)
            else:
                r = requests.get(url, headers=HEADERS)

            # if the status code is not 200, then raise the error
            r.raise_for_status()

            # use pyquery to parse html
            ret = self.parse(pq(r.text))

            if ret is None:
                raise ValueError('Failed to parse!')
        except requests.ConnectionError:
            self.logger.error("Connection Error.")
        except Exception as e:
            self.logger.error('%s', e.args)
            self.logger.error('Failed to crawl: %s', lang)
        else:
            self.logger.info('Done: %s', lang)
        return ret

    def run(self, langs=LANGUAGES):
        """
        Crawling the GitHub trending page of the language.

        :param langs: list of programming language names to be crawled
        """
        # get today's date
        today_date = datetime.datetime.now().strftime('%Y-%m-%d')
        filename = MD_FILE_NAME.format(name=today_date)

        # Create markdown file
        create_markdown(today_date, filename)

        descriptions = []
        for lang in langs:
            infos = self.crawl(lang)
            append_infos_to_md(filename, lang, infos)
            for info in infos:
                descriptions.append(info.desc)

        path = generate_wordcloud(descriptions=descriptions, filename=today_date)
        append_img_to_md(img_path=path, md_path=filename)
        self.logger.info("Finish crawling: %s", today_date)
