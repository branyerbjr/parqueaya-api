# Generated by Django 4.2.8 on 2023-12-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiservices', '0003_telegramsettings_chat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramsettings',
            name='chat_id',
        ),
        migrations.RemoveField(
            model_name='telegramsettings',
            name='id',
        ),
        migrations.AddField(
            model_name='telegramsettings',
            name='bot_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
