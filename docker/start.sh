#!/bin/bash

#pip install -r common.txt


#if [ -z "$DJANGO_SETTINGS_MODULE" ]
#then
    #pip install -r dev.txt
#else
    #pip install -r pre.txt
#fi

python /opt/app/manage.py collectstatic --noinput
python /opt/app/manage.py migrate

if [ -z "$TESTS" ]
then
    nginx -c /code/config/nginx.conf
    circusd  /code/config/circus.ini
else
    cd /opt/app/
    python manage.py test
fi


