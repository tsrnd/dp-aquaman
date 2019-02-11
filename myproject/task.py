from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from . import celeryconfig
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('yashoes')
app.config_from_object(celeryconfig, namespace='')
app.autodiscover_tasks()
