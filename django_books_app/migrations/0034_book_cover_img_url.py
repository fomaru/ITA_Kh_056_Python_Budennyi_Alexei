# Generated by Django 3.2.6 on 2021-08-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_books_app', '0033_remove_book_cover_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_img_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
