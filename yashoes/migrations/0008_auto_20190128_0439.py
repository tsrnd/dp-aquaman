# Generated by Django 2.1.5 on 2019-01-28 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yashoes', '0007_auto_20190128_0408'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('rate', 'user', 'product')},
        ),
    ]
