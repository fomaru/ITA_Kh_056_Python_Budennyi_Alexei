from django.contrib import admin
from .models import Book, Author, Review
from django_books_app.models import Comment

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Review)
admin.site.register(Comment)
