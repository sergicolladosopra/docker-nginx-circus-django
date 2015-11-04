from app.settings import *

INSTALLED_APPS += ('debug_toolbar',)


#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': os.environ.get('OPENSHIFT_APP_NAME'),
        #'USER': os.environ.get('OPENSHIFT_POSTGRESQL_DB_USERNAME'),
        #'PASSWORD': os.environ.get('OPENSHIFT_POSTGRESQL_DB_PASSWORD'),
        #'HOST': os.environ.get('OPENSHIFT_POSTGRESQL_DB_HOST'),
        #'PORT': os.environ.get('OPENSHIFT_POSTGRESQL_DB_PORT'),
    #}
#}
