# GitHub-Trending-Crawler

Crawling [GitHub Trending Pages](https://github.com/trending/) everyday.


## Introduction

The program is highly recommend to be deployed on a Linux server, which can crawl information about popular repositories of languages you are interested in on GitHub regulary. Then it will create a markdown file to record those information and generate a wordcloud image according to repositories' descriptions.

The spider is designed to help me keep track of the latest trends in technology and discover some new and interesting repositories. In fact, reading the newest markdown file has become a part of my daily routines. Besides, it can also increase contributions on GitHub :P

The idea was inspired by [LJ147](https://github.com/LJ147/GithubTrending).


## Installation

``` bash
$ wget https://github.com/fgksgf/GitHub-Trending-Crawler/archive/dev.zip
$ unzip dev.zip
$ rm dev.zip
$ cd GitHub-Trending-Crawler/
$ pip3 install -r requirements.txt
$ apt-get install python-tk python3-tk
```


## Usage

### Linux Server (Recommended)

#### 1. Git & SSH Configuration
[Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)

#### 2. Credential Storage
To make sure the spider don't need input username and password of your GitHub account when it use `git push`, credential Storage is necessary.

1. create a credential file to save your username and password.
``` bash
$ vim .git-credentials
```
2. Input the following content and save it, eg.`https://fgksgf:123456@github.com`
```
https://{username}:{password}@github.com
```
3. Use this command to save the credentials to a plain-text file on disk, and they never expire until you change your password for the Git host.
``` bash
$ git config --global credential.helper store
```

#### 3. Use Screen Command
1. Use the command to install screen
``` bash
$ sudo apt-get install screen (On Debian based Systems)
```
``` bash
$ sudo yum install screen (On RedHat based Systems)
```

2. Switch to the crawler directory and just type screen at the command prompt. Then the screen will show with interface exactly as the command prompt.
``` bash
$ screen
```

3. When you enter the screen, you can do all your work as you are in the normal CLI environment. But since the screen is an application, so it have command or parameters.

And now, we can run the program:
``` bash
$ python3 trending.py 
```
4. While the program is running, you can press “Ctrl-A” and “d“ to detach the screen. Then you can disconnect your SSH session.

5. When you want to check the status of the spider, just  start to SSH again to your server. .Then run this command to restore the screen:
``` bash
$ screen -r
```

For more inforamtion about screen command, you can visit [here](https://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/).


## ToDo List

- [ ] Refactor code with object-oriented methods
- [ ] Improve exception handling
- [ ] Add command-line usage feature
- [ ] Add logging feature

