# Generated by Django 3.2.6 on 2021-08-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_books_app', '0002_auto_20210814_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='django_books_app.Author'),
        ),
    ]
