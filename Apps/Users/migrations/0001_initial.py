# Generated by Django 2.2.6 on 2019-10-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('session_id', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
