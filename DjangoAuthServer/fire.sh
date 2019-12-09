#!/bin/bash

python /app/manage.py makemigrations 
python /app/manage.py migrate 
python /app/manage.py collectstatic --noinput
echo "launching uwsgi"
#uwsgi --ini /app/DjangoAuthServer/uwsgi.ini 
cd /app && gunicorn DjangoAuthServer.wsgi -b 0.0.0.0:8000 --timeout 300

