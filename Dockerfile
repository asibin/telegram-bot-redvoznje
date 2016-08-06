FROM python:alpine

MAINTAINER Sibin Arsenijevic "sibin.arsenijevic@gmail.com"

ADD . /telegram-bot-redvoznje

ENV PYTHONPATH /telegram-bot-redvoznje

WORKDIR /telegram-bot-redvoznje

RUN pip install -r requirements.txt

CMD ["python", "telegram-bot.py"]