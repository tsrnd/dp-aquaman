# Generated by Django 2.1.5 on 2019-01-16 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yashoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='yashoes.Product'),
        ),
    ]
