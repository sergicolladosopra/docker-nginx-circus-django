from app.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sqlite3.db'),
    }
}
INSTALLED_APPS += ('debug_toolbar', )

DEBUG = True
