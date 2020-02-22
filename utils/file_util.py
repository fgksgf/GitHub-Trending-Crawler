import codecs

import jieba
from wordcloud import WordCloud

from config import IMG_FILE_NAME, WC_BG_COLOR, WC_RANDOM_STATE, WC_FONT_PATH, WC_MARGIN, WC_HEIGHT, WC_WIDTH


def create_markdown(date, filename):
    """
    Create a markdown file.

    :param date: today's date.
    :param filename: the markdown file's name.
    """
    with open(filename, 'w') as f:
        f.write("# " + date + "\n")
        f.write("See what the GitHub community is most excited about.\n")


def generate_wordcloud(descriptions, filename):
    """
    Generate a wordcloud chart according to all descriptions of repositories.

    :param descriptions: a list contains all descriptions of today.
    :param filename: the name of wordcloud chart.
    """
    # join all strings in the list with ''
    text = ''.join(descriptions)

    # use jieba to do Chinese word segmentation first
    word_list = jieba.cut(text, cut_all=False)
    f = " ".join(word_list)

    # set the word cloud's attributes
    wc = WordCloud(background_color=WC_BG_COLOR,
                   width=WC_WIDTH,
                   height=WC_HEIGHT,
                   margin=WC_MARGIN,
                   font_path=WC_FONT_PATH,  # Use this font to ensure Chinese words can be shown
                   random_state=WC_RANDOM_STATE).generate(f)

    # save the chart as png file
    path = IMG_FILE_NAME.format(name=filename)
    wc.to_file(path)
    return path


def append_infos_to_md(filename, language, infos):
    """
    Append all repos' information of a language to the markdown file.

    :param filename: the markdown file's name
    :param language: the programming language
    :param infos: a dict contains all repos' information
    """
    # use codecs to solve the utf-8 encoding problem like Chinese
    with codecs.open(filename, "a", "utf-8") as f:
        f.write('\n## {language}\n'.format(language=language))
        for info in infos:
            f.write(info.convert_to_md())


def append_img_to_md(img_path, md_path):
    """
    Append an image of wordcloud to the markdown file.

    :param img_path: the image's path and name
    :param md_path: the markdown file's path and name
    """
    with codecs.open(md_path, "a", "utf-8") as f:
        f.write('\n## WordCloud\n')
        f.write('![]({path})\n'.format(path=img_path))
