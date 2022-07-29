# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Flask App Config
ENV APP_PORT 5555

# MySQL Config
ENV MYSQL_HOST 127.0.0.1
ENV MYSQL_PORT 3306
ENV MYSQL_USER admin
ENV MYSQL_PASSWORD ""
ENV MYSQL_DATABASE ""


CMD [ "python3", "app.py"]