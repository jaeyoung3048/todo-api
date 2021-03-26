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

AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'django-todo-ex'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)


DATA_UPLOAD_MAX_MEMORY_SIZE = 1024000000 # value in bytes 1GB here
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024000000

DEFAULT_FILE_STORAGE = 'mysite.asset_storage.S3DefaultStorage'
STATICFILES_STORAGE = 'mysite.asset_storage.S3StaticStorage'
