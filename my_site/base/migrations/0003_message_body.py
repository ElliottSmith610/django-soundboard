# Generated by Django 4.1.7 on 2023-02-27 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_person_message_alter_soundclip_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='body',
            field=models.TextField(default='Bruh'),
            preserve_default=False,
        ),
    ]