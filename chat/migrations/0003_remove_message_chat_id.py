# Generated by Django 2.2 on 2019-04-23 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_message_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chat_id',
        ),
    ]