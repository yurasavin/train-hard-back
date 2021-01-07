FROM python:3.8.5-buster

ENV PYTHONUNBUFFERED 1

ENV TERM=xterm

RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
