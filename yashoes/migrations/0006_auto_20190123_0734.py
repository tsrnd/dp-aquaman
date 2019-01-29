# Generated by Django 2.1.5 on 2019-01-23 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('yashoes', '0005_auto_20190122_0309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='transactions',
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_target_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='variants',
            field=models.ManyToManyField(through='yashoes.TransactionVariant', to='yashoes.Variant'),
        ),
        migrations.AlterModelTable(
            name='transactionvariant',
            table='transactions_variants',
        ),
    ]