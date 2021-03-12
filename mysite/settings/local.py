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

AWS_REGION = "ap-northeast-2"

AWS_STORAGE_BUCKET_NAME = 'django_todo_ex'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (
    AWS_STORAGE_BUCKET_NAME, AWS_REGION)

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_LOCATION = 'media'