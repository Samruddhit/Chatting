# Generated by Django 2.2 on 2019-04-23 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user_id',
        ),
    ]