# Generated by Django 3.2.8 on 2021-10-28 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20211028_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='previous',
            new_name='previous_post',
        ),
    ]
