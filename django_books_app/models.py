from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from martor.models import MartorField
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError


class Author(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey('Book', blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    review_text = models.TextField(max_length=1000, blank=False, validators=[MinLengthValidator(200)])
    create_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('review_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    comment_text = MartorField()

    def get_absolute_url(self):
        return reverse('review_list', kwargs={'pk': self.review.pk})

    def __str__(self):
        return self.comment_text


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True)
    authors = models.ManyToManyField('Author', blank=False)
    add_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover_img = models.ImageField(upload_to='images/', default='images/default_image.png')
    description = models.TextField(max_length=2000, validators=[MinLengthValidator(100)], blank=False)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

    class Meta:
        ordering = ['-id']

    def check_for_file(self):
        try:
            file = self.cover_img.file
            return True
        except FileNotFoundError:
            return False

    def __str__(self):
        return self.title


def authors_check(sender, **kwargs):
    if kwargs['instance'].authors.count() > 3:
        kwargs['instance'].delete()
        raise ValidationError("You can't assign more than three authors")


m2m_changed.connect(authors_check, sender=Book.authors.through)

