# Generated by Django 4.1.3 on 2023-06-23 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('uname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=30)),
                ('subject', models.EmailField(max_length=25)),
                ('messege', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='PaymentMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.CharField(max_length=20)),
                ('cvv', models.CharField(max_length=4)),
                ('expiry', models.CharField(max_length=20)),
                ('balance', models.FloatField(default=10000)),
            ],
            options={
                'db_table': 'PaymentMaster',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('price', models.FloatField(default=200)),
                ('description', models.CharField(max_length=50)),
                ('size', models.FloatField(default=1)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(default='abc.jpg', upload_to='Images')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.category')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
