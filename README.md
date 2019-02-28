# GitHub-Trending-Crawler

Crawling [GitHub Trending Pages](https://github.com/trending/) every day.


## Introduction

The program is highly recommend to be deployed on a Linux server with docker, which can crawl information about popular repositories of languages you are interested in on GitHub every day. Then it will create a markdown file to record those information and generate a wordcloud image according to repositories' descriptions.

The web crawler is designed to help me keep track of the latest trends in technology and discover some new and interesting repositories. In fact, reading the newest markdown file has become a part of my daily routines. Besides, it can also increase contributions on GitHub :P

The idea was inspired by [LJ147](https://github.com/LJ147/GithubTrending).

It requires the Python interpreter, **version 3.5+.**


## Installation

``` bash
$ wget https://github.com/fgksgf/GitHub-Trending-Crawler/archive/dev.zip
$ unzip dev.zip
$ rm dev.zip
$ cd GitHub-Trending-Crawler-dev/
```


## Usage on Linux Server

### with Docker (recommended)

#### 1. Git & SSH Configuration

+ **Fork my repo or create your own repo** for uploading the daily markdown file.

+ [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/). **No passphrase is recommended.**

#### 2. [Install Docker CE](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

#### 3. Use Docker

+ **In line sixth of the Dockerfile, enter your github username, email address and github repository url.**

+ Under the project directory, use this command to build a docker image:

``` bash
$ docker build -t gitcrawler --build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa)" --build-arg ssh_pub_key="$(cat ~/.ssh/id_rsa.pub)" .
```

+ Create a container and run it in the background, you will get a container id

``` bash
$ docker run -d gitcrawler:latest
```

+ For example, you get container id `ddf7f5f0379d` from last step, then type `docker logs ddf` to check logs.


### without Docker

``` bash
$ apt-get install python-tk python3-tk
$ virtualenv --no-site-packages env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ ssh-keyscan github.com > ~/.ssh/known_hosts
$ ssh-keyscan git.dev.tencent.com >> ~/.ssh/known_hosts
```

#### 1. Git & SSH Configuration (**ibid**)

#### 2. Use Screen Command

+ install screen

``` bash
# Debian based Systems
$ sudo apt-get install screen

# RedHat based Systems
$ sudo yum install screen
```

+ Switch to the repository directory and just type `screen` at the command prompt. Then the screen will show with interface exactly as the command prompt.

+ When you enter the screen, you can do all your work as you are in the normal CLI environment. But since the screen is an application, so it have command or parameters.

+ And now, we can run the program: `python3 trending.py`

+ _If you only want to get the markdown file, you can type `python3 trending.py -g off`._

+ _If you only want to run the program once, type `python3 trending.py -l off`._

+ While the program is running, you can press “Ctrl-A” and “d“ to detach the screen. Then you can disconnect your SSH session.

+ When you want to check the status of the spider, just start to SSH again to your server. Then run this command to restore the screen:

``` bash
$ screen -r
```

_For more information about screen command, you can visit [here](https://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/)._


## TODO

- [x] Add command-line usage feature
- [x] Dockerize the crawler
- [ ] Refactor code with object-oriented methods
- [ ] Improve exception handling
- [ ] Add logging feature

