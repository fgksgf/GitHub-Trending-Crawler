from crawler import GitHubCrawler

if __name__ == '__main__':
    crawler = GitHubCrawler()
    crawler.run(langs=['java'])
