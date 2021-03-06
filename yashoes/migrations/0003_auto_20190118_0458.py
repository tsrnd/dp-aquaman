# Generated by Django 2.1.5 on 2019-01-18 04:58

from django.db import migrations, models
import yashoes.model.variant
import yashoes.models


class Migration(migrations.Migration):

    dependencies = [
        ('yashoes', '0002_auto_20190117_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_profile',
            field=models.ImageField(blank=True, max_length=50000, null=True, upload_to=yashoes.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='variant',
            name='image_link',
            field=models.ImageField(blank=True, max_length=50000, null=True, upload_to=yashoes.model.variant.get_image_path),
        ),
    ]
