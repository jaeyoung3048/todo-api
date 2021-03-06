from mysite.settings.base import *
from utils.secrets import *

DEBUG = True

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'todo_example',
        'USER': 'root',
        'PASSWORD': get_secret('DATABASES_PASSWORD'),
        'HOST': "localhost",
        'PORT': '3306',
    }
}