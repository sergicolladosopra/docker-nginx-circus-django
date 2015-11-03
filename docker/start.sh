#!/bin/bash

python /code/app/manage.py collectstatic
nginx -c /code/config/nginx.conf
circusd  /code/app/circus.ini
