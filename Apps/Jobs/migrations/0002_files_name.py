# Generated by Django 2.2.6 on 2019-11-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
