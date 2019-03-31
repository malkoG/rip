FROM python:3


RUN apt-get update &&\
    apt-get -y install \
    libpq-dev \
    python-dev

WORKDIR /app

ADD ./manage.py    /app/
ADD ./Pipfile      /app/
ADD ./Pipfile.lock /app/

ADD pip install pipenv

RUN pipenv install

RUN python manage.py runserver