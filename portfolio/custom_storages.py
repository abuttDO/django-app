from django.conf import settings
from storages.backends.s3boto3 import S#Boto3Storage

class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION