# Generated by Django 3.2.6 on 2021-08-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_books_app', '0010_book_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
