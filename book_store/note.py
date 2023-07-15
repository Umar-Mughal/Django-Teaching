# A custom note file just to record stuff executed on python interactive shell!

# --- INSERTION --- #
from book_outlet.models import Book

harry_potter = Book(title="Harry Potter", rating=5, author="dont know", is_bestselling=True)
harry_potter.save()  # Here actual DB query is executed

# --- RETRIEVING ALL --- #
Book.objects.all()

# --- UPDATING --- #
harry_potter = Book.objects.all()[0]
harry_potter.author = "J.K Rowling"
harry_potter.title = "Harry Potter 1"
harry_potter.save()

