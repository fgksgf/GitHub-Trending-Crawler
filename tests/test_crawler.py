from unittest import TestCase

from crawler import GitHubCrawler


class TestGitHubCrawler(TestCase):
    def test_crawl(self):
        crawler = GitHubCrawler()
        self.assertIsNotNone(crawler.crawl('python', 'daily'))
        self.assertIsNotNone(crawler.crawl('c', 'weekly'))
        self.assertIsNotNone(crawler.crawl('java', 'monthly'))

    def test_run(self):
        self.fail()
