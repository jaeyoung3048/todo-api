from mysite.settings.base import *
from utils.secrets import *

DEBUG = False

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo_api',
        'USER': 'postgres',
        'PASSWORD': get_secret('RDS_DATABASES_PASSWORD'),
        'HOST': get_secret('RDS_DATABASE_HOST'),
        'PORT': '5432',
    }
}

AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'django-todo-api'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)


DATA_UPLOAD_MAX_MEMORY_SIZE = 1024000000 # value in bytes 1GB here
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024000000

DEFAULT_FILE_STORAGE = 'mysite.asset_storage.S3DefaultStorage'
STATICFILES_STORAGE = 'mysite.asset_storage.S3StaticStorage'
