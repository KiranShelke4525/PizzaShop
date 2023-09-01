# Generated by Django 4.1.3 on 2023-08-27 15:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0006_delete_paymenthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(default=datetime.datetime.now)),
                ('amount_paid', models.FloatField()),
                ('payment_method', models.CharField(max_length=50)),
                ('transaction_id', models.CharField(max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.paymentmaster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.userinfo')),
            ],
            options={
                'db_table': 'PaymentHistory',
            },
        ),
    ]