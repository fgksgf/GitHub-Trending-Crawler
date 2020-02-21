class RepoInfo:
    """
    Information of the repository.
    """

    GITHUB_URL = 'https://github.com'

    def __init__(self, href, stars, desc):
        # href: '/Username/RepoName'
        p = href.rindex('/')

        # owner of the repository
        self.owner = href[:p]

        # name of the repository
        self.name = href[p + 1:]

        # the complete url of the repository
        self.url = self.GITHUB_URL + href

        # the number of stars it got
        self.stars = stars

        # description of the repository
        self.desc = desc
