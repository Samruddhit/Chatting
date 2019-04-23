# Generated by Django 2.2 on 2019-04-18 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_alive',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='key_expires',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='terms_condition',
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='participants',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_of_chat', to=settings.AUTH_USER_MODEL),
        ),
    ]