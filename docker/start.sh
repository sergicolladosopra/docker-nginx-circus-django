#!/bin/bash

python /opt/app/manage.py collectstatic --noinput
python /opt/app/manage.py migrate
nginx -c /code/config/nginx.conf
circusd  /code/config/circus.ini
