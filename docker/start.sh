#!/bin/bash

python /opt/app/manage.py collectstatic --noinput
nginx -c /code/config/nginx.conf
circusd  /code/config/circus.ini
