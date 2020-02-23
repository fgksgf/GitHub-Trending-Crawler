from unittest import TestCase

from crawler import GitHubCrawler


class TestGitHubCrawler(TestCase):
    def test_crawl(self):
        crawler = GitHubCrawler()
        self.assertIsNotNone(crawler.crawl('python'))
        self.assertIsNotNone(crawler.crawl('c'))
        self.assertIsNotNone(crawler.crawl('java'))

    def test_run(self):
        # TODO: check if the markdown file and the wordcloud image exist
        self.assertTrue(True)
