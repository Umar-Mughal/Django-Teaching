# A custom note file just to record stuff executed on python interactive shell!

# --- INSERTION --- #
from book_outlet.models import Book

harry_potter = Book(title="Harry Potter", rating=5, author="dont know", is_bestselling=True)
harry_potter.save()  # Here actual DB query is executed
