import codecs


def create_markdown(date, filename):
    """
    Create a markdown file.

    :param date: today's date.
    :param filename: the markdown file's name.
    """
    with open(filename, 'w') as f:
        f.write("# " + date + "\n")
        f.write("See what the GitHub community is most excited about.\n")


def generate_word_cloud(content_list, date):
    """
    Generate a word cloud picture according to all descriptions of today.
    Then save the picture at 'img/', which is named by date.

    :param content_list: a list contains all descriptions of today.
    :param date: today's date.
    """
    # Join all strings in the list with ''
    text = ''.join(content_list)

    # Use jieba to do Chinese word segmentation first
    word_list = jieba.cut(text, cut_all=False)
    f = " ".join(word_list)

    # Set the word cloud's attributes
    wc = WordCloud(background_color="white",
                   width=800,
                   height=600,
                   margin=2,
                   font_path='MSYH.TTC',  # Use this font to ensure Chinese words can be shown
                   random_state=20).generate(f)

    # Save the picture
    wc.to_file('img/{date}.png'.format(date=date))


def append_infos_to_md(filename, language, infos):
    """
    Append all repos' information of a language to the markdown file.

    :param filename: the markdown file's name
    :param language: the programming language
    :param infos: a dict contains all repos' information
    """
    # Use codecs to solve the utf-8 encoding problem like Chinese
    with codecs.open(filename, "a", "utf-8") as f:
        f.write('\n## {language}\n'.format(language=language))
        for repo in infos:
            f.write(repo)


def append_img_to_md(filename, date):
    """
    Append an image of word cloud based on all descriptions
    to the markdown file.

    :param filename: the markdown file's name
    :param date: today's date, the image's name as well
    """
    img_path = 'img/{date}.png'.format(date=date)
    with codecs.open(filename, "a", "utf-8") as f:
        f.write('\n## WordCloud\n')
        f.write('![]({path})\n'.format(path=img_path))
