# Generated by Django 3.2.8 on 2021-10-29 10:04

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20211028_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Commentaire'),
        ),
    ]