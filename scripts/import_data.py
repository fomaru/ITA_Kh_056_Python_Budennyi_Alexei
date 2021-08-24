from django_books_app import models
import json
from django.templatetags.static import static
import random

def run():

    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris semper tellus mauris, id accumsan erat tincidunt ultricies. Donec lacinia felis sit amet suscipit mattis. Donec eu fringilla quam. Pellentesque consequat varius tortor in elementum. Phasellus enim augue, aliquam efficitur imperdiet id, efficitur quis neque. Donec lectus dolor, feugiat vitae sagittis non, placerat at lacus. Suspendisse ac aliquam felis. Duis fermentum sapien ac nisi faucibus, a consectetur ligula tempor. Mauris condimentum metus a dolor ultricies facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla id massa gravida, sagittis sapien quis, aliquam tortor. Sed euismod leo ut semper laoreet. Cras non mollis magna, a porta nunc. Pellentesque eros ante, ultrices in ipsum ut, vehicula placerat sem. Proin accumsan blandit massa vel hendrerit."

    with open(file='scripts/data.json', mode='r') as file:
        data = json.load(file)

    for book in data:
        if models.Book.objects.filter(title__exact=book['title']).exists():
            pass
        else:
            authors = []
            for author in book['authors']:
                if models.Author.objects.filter(name__exact=author).exists():
                    authors.append(models.Author.objects.filter(name__exact=author)[0])
                else:
                    new_author = models.Author(name=author)
                    new_author.save()
                    authors.append(models.Author.objects.filter(name__exact=author)[0])
            if 'longDescription' in book and len(book['longDescription']) >= 100:
                desc = book['longDescription']
            else:
                desc = lorem
            new_book = models.Book(title=book['title'],
                                   description=desc,
                                   rating=random.randint(1, 10),
                                   added_by=models.User.objects.get(pk=1))
            new_book.save()
            if 'thumbnailUrl' in book:
                new_book.cover_img = book['thumbnailUrl']
            new_book.authors.set(authors)
            new_book.save()

