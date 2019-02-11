from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from . import celeryconfig
from django.apps import apps
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('yashoes')
app.config_from_object(celeryconfig, namespace='')
# app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
app.autodiscover_tasks(settings.INSTALLED_APPS)
