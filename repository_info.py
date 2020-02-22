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

        # status about how many stars it got, a string
        self.star_status = stars

        # description of the repository
        self.desc = desc

    def convert_to_md(self):
        """
        Convert repository info into markdown format.

        :return:
        """
        pattern = u"+ [{name}]({url})(**{stars}**): {desc}\n"
        return pattern.format(name=self.name, url=self.url, desc=self.desc, stars=self.star_status)

    def __str__(self):
        return str({'name': self.name, 'url': self.url, 'star_status': self.star_status, 'desc': self.desc})
