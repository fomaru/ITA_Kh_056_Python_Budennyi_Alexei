# Generated by Django 3.2.6 on 2021-08-21 08:43

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_books_app', '0035_remove_book_cover_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=martor.models.MartorField(),
        ),
    ]
