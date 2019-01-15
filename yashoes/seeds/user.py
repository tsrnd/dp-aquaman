from django.contrib.auth import get_user_model

CONST_ADMIN_LIST = [
    {
        'username': 'anhngo',
        'email': 'anh.ngo@asiantech.vn',
        'password': 'anhngo',
    },
    {
        'username': 'chaunguyen',
        'email': 'chau.nguyen@asiantech.vn',
        'password': 'chaunguyen',
    },
    {
        'username': 'hoanguyen',
        'email': 'hoa.nguyen@asiantech.vn',
        'password': 'hoanguyen',
    },
    {
        'username': 'minhdao',
        'email': 'minh.dao@asiantech.vn',
        'password': 'minhdao',
    },
    {
        'username': 'phutran',
        'email': 'phu.tran@asiantech.vn',
        'password': 'phutran',
    },
    {
        'username': 'sonvu',
        'email': 'son.vu@asiantech.vn',
        'password': 'sonvu',
    },
    {
        'username': 'tamnguyen',
        'email': 'tam.nguyen@asiantech.vn',
        'password': 'tamnguyen',
    },
    {
        'username': 'thachnguyen',
        'email': 'thach.nguyen@asiantech.vn',
        'password': 'thachnguyen',
    },
    {
        'username': 'thaile',
        'email': 'thai.le@asiantech.vn',
        'password': 'thaile',
    },
    {
        'username': 'yenho',
        'email': 'yen.ho@asiantech.vn',
        'password': 'yenho',
    },
]

def create_superuser():
    User = get_user_model()
    for data in CONST_ADMIN_LIST:
        try:
            User.objects.get(username=data.get('username'))
        except:
            User.objects.create_superuser(**data)
