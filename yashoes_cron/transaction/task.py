from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# from myproject import task_app
#
#
# RESULT_LIMIT = 10000
#
#
# # @shared_task
# @task_app.task
# def update_shipping():
#     from datetime import timedelta
#     from django.utils import timezone
#     from yashoes.model.notification import Notification
#     from django.db import DatabaseError, transaction
#     from django.contrib.contenttypes.models import ContentType
#     from yashoes.model.transaction import Transaction
#
#     try:
#         while True:
#             with transaction.atomic():
#                 nested_q_trans = Transaction.objects.filter(status=1, deleted_at=None).order_by('-updated_at')[:RESULT_LIMIT]
#                 d = 0
#                 if nested_q_trans:
#                     Transaction.objects.filter(pk__in=nested_q_trans).update(status=2, updated_at=timezone.now())
#                     for tran in nested_q_trans:
#                         Notification.objects.create(
#                             user_id=tran.user_id,
#                             content='shipping',
#                             notification_type=ContentType.objects.get_for_model(tran),
#                             notification_target_id=tran.pk,
#                             notify_datetime=timezone.now(),
#                         )
#                     print(f'Update {RESULT_LIMIT * d + len(nested_q_trans)} records successfull')
#                     d = d + 1
#                     continue
#                 break
#     except DatabaseError as derr:
#         print('Database has an error. ', derr)
#     except Exception as err:
#         print('System has an error. ', err)

from celery import shared_task
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')


@shared_task(bind=True)
def test():
    print("AIHHIHIH")
