# Generated by Django 4.1.3 on 2023-08-27 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0007_paymenthistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentHistory',
        ),
    ]