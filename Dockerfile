FROM python:3-buster

MAINTAINER Guilhem Allaman "dev@guilhemallaman.net"

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]