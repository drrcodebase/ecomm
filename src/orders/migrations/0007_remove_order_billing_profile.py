# Generated by Django 2.2.3 on 2019-08-28 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190828_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_profile',
        ),
    ]