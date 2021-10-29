# Generated by Django 3.2.8 on 2021-10-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='Nombre de vue'),
        ),
        migrations.AlterField(
            model_name='post',
            name='comment_count',
            field=models.IntegerField(default=0, verbose_name='Nombre de commentaire'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='', verbose_name='Article Image'),
        ),
    ]