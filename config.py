# programming languages you are interested in
LANGUAGES = ['python', 'java', 'unknown', 'javascript', 'html', 'go']

# frequency of trending
FREQUENCY = ['daily', 'weekly', 'monthly']

# wordcloud chart config
WC_BG_COLOR = 'white'  # background color
WC_WIDTH = 800
WC_HEIGHT = 600
WC_MARGIN = 2
WC_FONT_PATH = 'MSYH.TTC'  # use this font to ensure Chinese words can be shown
WC_RANDOM_STATE = 20

# proxy pool api
PROXY_POOL_API = {
    'get_a_proxy': '',
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

TRENDING_URL = 'https://github.com/trending/{language}?since={frequency}'

MD_FILE_NAME = '{name}.md'

IMG_FILE_NAME = 'img/{name}.png'
