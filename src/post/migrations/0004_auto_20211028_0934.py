# Generated by Django 3.2.8 on 2021-10-28 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20211027_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='next_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='suivant', to='post.post', verbose_name='suivant'),
        ),
        migrations.AddField(
            model_name='post',
            name='previous',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='precedant', to='post.post', verbose_name='precedent'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='post.Category', verbose_name='Categorie'),
        ),
    ]
