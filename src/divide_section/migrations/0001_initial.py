# Generated by Django 3.2.8 on 2021-10-27 12:02

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DivideSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Titre de la section divide')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Partie section',
                'verbose_name_plural': 'Partie section',
            },
        ),
    ]
