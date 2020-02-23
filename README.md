# GitHub-Trending-Crawler

Crawling [GitHub Trending Pages](https://github.com/trending/) every day.

## Introduction

The program is highly recommend to be deployed on a Linux server, which can crawl information about popular repositories of languages you are interested in on GitHub every day. Then it will create a markdown file to record those information and generate a wordcloud image according to repositories' descriptions.

This crawler is designed to help me keep track of the latest trends in technology and discover some new and interesting repositories. In fact, reading the newest markdown file has become a part of my daily routines. More importantly, it increases contributions of GitHub :P

The idea was inspired by [LJ147](https://github.com/LJ147/GithubTrending).

## Requirements

+   python 3.6+
+   git
+   screen
+   unzip

## Configuration

+ **Fork my repo or create your own repo** for uploading markdown files.

+ If you don't have ssh keys, [generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/). 

## Usage on Linux

The `release` branch is stable, and there is only code. 

``` bash
$ sudo apt install -y unzip screen
$ wget https://github.com/fgksgf/GitHub-Trending-Crawler/archive/release.zip
$ unzip release.zip
$ cd GitHub-Trending-Crawler-release/
$ apt-get install python-tk python3-tk
$ pip3 install -r requirements.txt
```

1. Switch to the repository directory and just type `screen` at the command prompt. Then the screen will show with interface exactly as the command prompt.

2. When you enter the screen, you can do all your work as you are in the normal CLI environment. But since the screen is an application, so it have command or parameters.

3. And now, we can run the program: `python3 main.py -p -l`

4. While the program is running, you can press `Ctrl + A` and `d` to detach the screen. Then you can disconnect your SSH session.

5. When you want to check the status of the crawler, just reconnect to your server via ssh. Then use this command  `screen -r` to restore the screen. _For more information about `screen` command, you can visit [here](https://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/)._

## CLI Options

```bash
python3 main.py (-h | --help)
python3 main.py (-v | --version)
python3 main.py [-l | --loop] [-p | --push] [--frequency=<f>]

Options:
  -h --help        Show this screen.
  -v --version     Show version.
  -l --loop        Run this program cyclically.
  -p --push        Use git to push the markdown and the image.
  --frequency=<f>  The frequency of crawling [default: daily].
```

## Change Logs

### V1.5 (2020-02-22)

+ Refactor code with object-oriented methods
+ Split single python file into several files
+ Improve exception handling
+ Add logging feature
+ Use `docopt` to enhance command-line usage
+ Update requirements
