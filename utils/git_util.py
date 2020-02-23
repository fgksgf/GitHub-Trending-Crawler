import datetime
import os

from config import MD_FILE_NAME, IMG_FILE_NAME


def git_add_commit_push():
    """
    Upload the markdown file and the image to GitHub by git.
    """
    date = datetime.datetime.now().strftime('%Y-%m-%d')

    md_name = MD_FILE_NAME.format(name=date)
    img_name = IMG_FILE_NAME.format(name=date)

    cmd_git_add = 'git add {file1} && git add {file2}'.format(file1=md_name, file2=img_name)
    cmd_git_commit = 'git commit -m "{date}"'.format(date=date)
    cmd_git_push = 'git push -u origin master'

    os.system(cmd_git_add)
    os.system(cmd_git_commit)
    os.system(cmd_git_push)
