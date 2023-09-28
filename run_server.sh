#!/bin/sh

python manage.py makemigrations
until python manage.py migrate
do
    echo "Waiting for db to be ready..."
done


python manage.py collectstatic --noinput;
gunicorn -w 2 -b 0:8000 myproject.wsgi;
