#!/bin/bash

sleep 3
echo "launching uwsgi"
#uwsgi --ini /app/DjangoAppServer/uwsgi.ini 
cd /app && gunicorn DjangoAppServer.wsgi -b 0.0.0.0:8000 --timeout 300
sleep 600
