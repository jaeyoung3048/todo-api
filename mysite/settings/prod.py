from mysite.settings.base import *
from utils.secrets import *

DEBUG = False

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'todo_api',
        'USER': 'root',
        'PASSWORD': get_secret('DATABASES_PASSWORD'),
        'HOST': get_secret('DATABASES_HOST'),
        'PORT': '3306',
    }
}