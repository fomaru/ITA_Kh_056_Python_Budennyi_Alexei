# Generated by Django 3.2.6 on 2021-08-15 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_books_app', '0003_auto_20210815_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]
