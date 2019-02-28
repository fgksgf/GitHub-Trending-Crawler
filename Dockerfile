FROM python:3.5-slim
MAINTAINER  Hoshea Jiang <fgksgf@yahoo.com>

ARG ssh_prv_key
ARG ssh_pub_key
ENV USERNAME=fgksgf \
    EMAIL=fgksgf@yahoo.com \
    URL=git@git.dev.tencent.com:zerone01/Github-Trending-Crawler.git

COPY ./trending.py ./MSYH.TTC ./requirements.txt /code/

WORKDIR /code

RUN apt-get update && \
    apt-get install -y git && \
    mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts && \
    ssh-keyscan git.dev.tencent.com >> /root/.ssh/known_hosts && \
    echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub && \
    git config --global user.name $USERNAME && \
    git config --global user.email $EMAIL && \
    mkdir img && \
    pip install -r requirements.txt && \
    git init && \
    git remote add origin $URL && \
    git pull origin master

CMD ["python", "trending.py"]