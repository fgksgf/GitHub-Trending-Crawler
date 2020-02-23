FROM python:3.6-slim
MAINTAINER  Hoshea Jiang <fgksgf@gmail.com>

ENV URL=<YourGitHubRepositoryUrl>

WORKDIR /code

RUN apt-get update && \
    apt-get install -y git && \
    mkdir img && \
    pip install -r requirements.txt && \
    git init && \
    git remote add origin $URL && \
    git pull origin master

CMD ["python", "main.py", "-p", "-l"]
