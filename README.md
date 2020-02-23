# GitHub-Trending-Crawler

Crawling [GitHub Trending Pages](https://github.com/trending/) every day.

## Introduction

The program is highly recommend to be deployed on a Linux server with docker, which can crawl information about popular repositories of languages you are interested in on GitHub every day. Then it will create a markdown file to record those information and generate a wordcloud image according to repositories' descriptions.

This crawler is designed to help me keep track of the latest trends in technology and discover some new and interesting repositories. In fact, reading the newest markdown file has become a part of my daily routines. More importantly, it increases contributions of GitHub :P

The idea was inspired by [LJ147](https://github.com/LJ147/GithubTrending).

## Installation

The `release` branch is stable, and there is only code. 

``` bash
$ wget https://github.com/fgksgf/GitHub-Trending-Crawler/archive/dev.zip
$ unzip dev.zip
$ rm dev.zip
$ cd GitHub-Trending-Crawler-dev/
```

## Usage on Linux

```bash
python  main.py (-h | --help)
python  main.py (-v | --version)
python  main.py [-l | --loop] [-p | --push] [--frequency=<f>]

Options:
  -h --help        Show this screen.
  -v --version     Show version.
  -l --loop        Run this program cyclically.
  -p --push        Use git to push the markdown and the image.
  --frequency=<f>  Speed in knots [default: daily].
```

### With Docker (Recommended)

#### 1. Git & SSH Configuration

+ **Fork my repo or create your own repo** for uploading the daily markdown file.

+ If you don't have ssh keys, [generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/). 

#### 2. [Install Docker CE](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

#### 3. Use Docker

+ **In line fourth of the Dockerfile, enter your github repository url.**

+ Under the project directory, use this command to build a docker image:

``` bash
$ docker build -t gitcrawler .
```

+ Create a container and run it in the background, you will get a container id

``` bash
$ docker run -d gitcrawler:latest -v /<YourAbsolutePath>/GitHub-Trending-Crawler:/code -v ~/.ssh:/root/.ssh
```

+ Then use  `docker logs <container id>` to check logs.


### Without Docker

``` bash
$ apt-get install python-tk python3-tk
$ pip3 install -r requirements.txt
```

#### 1. Git & SSH Configuration (**ibid**)

#### 2. Use Screen Command

+ install screen

``` bash
# Debian based Systems
$ sudo apt-get install -y screen

# RedHat based Systems
$ sudo yum install screen
```

+ Switch to the repository directory and just type `screen` at the command prompt. Then the screen will show with interface exactly as the command prompt.

+ When you enter the screen, you can do all your work as you are in the normal CLI environment. But since the screen is an application, so it have command or parameters.

+ And now, we can run the program: `python3 main.py -p -l`

+ While the program is running, you can press “Ctrl-A” and “d“ to detach the screen. Then you can disconnect your SSH session.

+ When you want to check the status of the crawler, just reconnect to your server via ssh. Then use this command  `screen -r` to restore the screen.

_For more information about `screen` command, you can visit [here](https://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/)._


## Change Logs

### V1.5 (2020-02-22)

+ Refactor code with object-oriented methods
+ Split single python file into several files
+ Improve exception handling
+ Add logging feature
+ Mount code rather than copy code into docker image
+ Use `docopt` to enhance command-line usage
+ Update requirements
