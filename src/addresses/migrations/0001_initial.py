# Generated by Django 2.2.3 on 2019-08-27 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0002_auto_20190823_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addess_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120)),
                ('address_line_1', models.CharField(max_length=120)),
                ('address_line_2', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(default='United Kingdom', max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('postel_code', models.CharField(max_length=120)),
                ('billing_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile')),
            ],
        ),
    ]