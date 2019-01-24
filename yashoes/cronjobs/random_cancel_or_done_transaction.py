from datetime import timedelta
from django.utils import timezone
from yashoes.model.transaction import Transaction
from yashoes.model.notification import Notification
from django.db import DatabaseError, transaction
from django.contrib.contenttypes.models import ContentType
import random
import math
import time

def random_cancel_done_transaction():
    nested_q_trans_delivery = Transaction.objects.filter(status=2, deleted_at=None, updated_at__gte=timezone.now()-timedelta(days=3))
    nested_q_trans_inprocess = Transaction.objects.filter(status=1, deleted_at=None, updated_at__gte=timezone.now()-timedelta(days=3))
    total_delivery = nested_q_trans_delivery.count()
    total_inprocess = nested_q_trans_inprocess.count()
    total_inprocess_to_cancel = math.floor(total_inprocess*0.25)
    total_delivery_to_cancel = math.floor(total_delivery*0.25)
    total_delivery_to_done = total_delivery - total_delivery_to_cancel
    try:
        with transaction.atomic():
            inprocessing_to_cancel = random.sample(list(nested_q_trans_inprocess),k=total_inprocess_to_cancel)
            print(type(inprocessing_to_cancel), inprocessing_to_cancel)
            if len(inprocessing_to_cancel) > 0:
                arr_id_trans = []
                arr_notification = []
                for tran in inprocessing_to_cancel:
                    arr_id_trans.append(tran.id)
                    arr_notification.append(Notification(
                            user_id=tran.user_id,
                            content='cancel',
                            notification_type=ContentType.objects.get_for_model(tran),
                            notification_target_id=tran.pk,
                            notify_datetime=timezone.now(),
                        )
                    )
                Transaction.objects.filter(pk__in=arr_id_trans).update(status=4, updated_at=timezone.now())
                Notification.objects.bulk_create(arr_notification)
                print(f'\n_______Update {total_inprocess_to_cancel} records from in processing to cancel successfull_______\n')
    except DatabaseError as derr:
        print('Database has an error. ', derr)
        return
    except Exception as err:
        print('System has an error. ', err)
        return
    
    try:
        with transaction.atomic():
            delivery_to_cancel = random.sample(list(nested_q_trans_delivery),k=total_delivery_to_cancel)
            if delivery_to_cancel:
                arr_id_trans = []
                arr_notification = []
                for tran in delivery_to_cancel:
                    arr_id_trans.append(tran.id)
                    arr_notification.append(Notification(
                            user_id=tran.user_id,
                            content='cancel',
                            notification_type=ContentType.objects.get_for_model(tran),
                            notification_target_id=tran.pk,
                            notify_datetime=timezone.now(),
                        )
                    )
                Transaction.objects.filter(pk__in=arr_id_trans).update(status=4, updated_at=timezone.now())
                Notification.objects.bulk_create(arr_notification)
                print(f'\n_______Update {total_delivery_to_cancel} records from delivery to cancel successfull_______\n')
    except DatabaseError as derr:
        print('Database has an error. ', derr)
        return
    except Exception as err:
        print('System has an error. ', err)
        return
        
    try:
        with transaction.atomic():
            delivery_to_done = list(set(nested_q_trans_delivery).difference(delivery_to_cancel))
            if delivery_to_done:
                arr_id_trans = []
                arr_notification = []
                for tran in delivery_to_done:
                    arr_id_trans.append(tran.id)
                    arr_notification.append(Notification(
                            user_id=tran.user_id,
                            content='done',
                            notification_type=ContentType.objects.get_for_model(tran),
                            notification_target_id=tran.pk,
                            notify_datetime=timezone.now(),
                        )
                    )
                Transaction.objects.filter(pk__in=arr_id_trans).update(status=3, updated_at=timezone.now())                
                Notification.objects.bulk_create(arr_notification)
                print(f'\n_______Update {total_delivery_to_done} records from delivery to done successfull_______\n')
    except DatabaseError as derr:
        print('Database has an error. ', derr)
    except Exception as err:
        print('System has an error. ', err)
        