import os


def git_add_commit_push(date, filename):
    """
    Upload the markdown file and the image to GitHub by git.

    :param date: today's date.
    :param filename: the markdown file's name.
    """
    cmd_git_add_md = 'git add {filename}'.format(filename=filename)
    cmd_git_add_img = 'git add img/{date}.png'.format(date=date)
    cmd_git_commit = 'git commit -m "{date}"'.format(date=date)
    cmd_git_push = 'git push -u origin master'

    os.system(cmd_git_add_md)
    os.system(cmd_git_add_img)
    os.system(cmd_git_commit)
    os.system(cmd_git_push)
