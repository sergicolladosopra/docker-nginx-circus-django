#!/bin/bash

python /code/app/manage.py collectstatic --noinput
nginx -c /code/config/nginx.conf
circusd  /code/app/circus.ini
