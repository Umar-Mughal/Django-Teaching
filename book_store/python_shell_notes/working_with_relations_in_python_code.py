# First Creating an Author Record in DB
from book_outlet.models import Book, Author
jkrowlings = Author(first_name="J.K", last_name="Rowling")
jkrowlings.save()
Author.objects.all()[0].first_name
>>> 'J.K'

# Now Creating a Book Record in DB with Author as Foreign Key
hp1 = Book(title="Harry Potter 1", rating=5, is_bestselling=True, slug="harry-potter-1", author=jkrowlings)
hp1.save()
Book.objects.all()
>>> <QuerySet [<Book: Harry Potter 1 (Rating:5)>]>

# Getting Book's Author Data
harrypotter1 = Book.objects.get(title="Harry Potter 1")
harrypotter1.author
>>> <Author: Author object (1)>
harrypotter1.author.first_name
>>> 'J.K'
