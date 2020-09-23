import datetime
import posixpath

from django.conf import settings


def get_image_upload_path(instance, filename):
    return posixpath.join(datetime.datetime.now().strftime(settings.IMAGE_FOLDER), filename)


def get_default_currency():
    """
    For use as the default value for currency fields.  Use of this function
    prevents Django's core migration engine from interpreting a change to
    OSCAR_DEFAULT_CURRENCY as something it needs to generate a migration for.
    """
    return settings.DEFAULT_CURRENCY
