#!/bin/sh

pip install pipenv
pipenv install

python manage.py migrate
gunicorn --workers=3 --bind 0:8000 restinpeace.wsgi
