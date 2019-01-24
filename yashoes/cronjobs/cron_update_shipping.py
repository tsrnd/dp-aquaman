import time
from datetime import timedelta
from django.utils import timezone
from yashoes.model.transaction import Transaction
from yashoes.model.notification import Notification
from django.db import DatabaseError, transaction
from django.contrib.contenttypes.models import ContentType

RESULT_LIMIT = 10000
def update_shipping():
    try:
        while True:
            with transaction.atomic():
                nested_q_trans = Transaction.objects.filter(status=1, deleted_at=None, updated_at__gte=timezone.now()-timedelta(days=3)).order_by('-updated_at')[:RESULT_LIMIT]
                d = 0
                if nested_q_trans:
                    Transaction.objects.filter(pk__in=nested_q_trans).update(status=2, updated_at=timezone.now())
                    for tran in nested_q_trans:
                        Notification.objects.create(
                            user_id=tran.user_id,
                            content='shipping',
                            notification_type=ContentType.objects.get_for_model(tran),
                            notification_target_id=tran.pk,
                            notify_datetime=timezone.now(),
                        )
                    print(f'Update {RESULT_LIMIT*d+len(nested_q_trans)} records successfull')
                    d=d+1
                    continue
                break
    except DatabaseError as derr:
        print('Database has an error. ', derr)
    except Exception as err:
        print('System has an error. ', err)
        