import datetime
import os


def git_add_commit_push():
    """
    Upload the markdown file and the image to GitHub by git.
    """
    date = datetime.datetime.now().strftime('%Y-%m-%d')

    cmd_git_add = 'git add .'
    cmd_git_commit = 'git commit -m "{date}"'.format(date=date)
    cmd_git_push = 'git push -u origin master'

    os.system(cmd_git_add)
    os.system(cmd_git_commit)
    os.system(cmd_git_push)
