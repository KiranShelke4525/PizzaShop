# Generated by Django 4.1.3 on 2023-08-27 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_paymenthistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentHistory',
        ),
    ]