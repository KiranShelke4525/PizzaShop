# Generated by Django 4.1.3 on 2023-08-27 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_paymenthistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentHistory',
        ),
    ]
