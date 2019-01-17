# Generated by Django 2.1.5 on 2019-01-17 04:23

from django.db import migrations, models
import django.db.models.deletion
import yashoes.model.version


class Migration(migrations.Migration):

    dependencies = [
        ('yashoes', '0002_auto_20190116_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='image_link',
            field=models.ImageField(blank=True, default='yashoes/static/product/None/no-imgage.png', null=True, upload_to=yashoes.model.version.get_image_path),
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='yashoes.Product'),
        ),
    ]
