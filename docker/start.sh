#!/bin/bash

python /opt/app/manage.py collectstatic
nginx -c /code/config/nginx.conf
circusd  /code/config/circus.ini
