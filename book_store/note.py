# A custom note file just to record stuff executed on python interactive shell!

# ------------------------------------------------------------ #
# --- INSERTING --- #
from book_outlet.models import Book

# -- inserting option 1: Model.save() method -- #
harry_potter = Book(title="Harry Potter", rating=5, author="dont know", is_bestselling=True)
harry_potter.save()  # Here actual DB query is executed
# -- inserting option 2: Model.objects.create() method -- #
Book.objects.create(title="Harry Potter", rating=2, author="J.K Rowlings", is_bestselling=True)

# ------------------------------------------------------------ #
# --- RETRIEVING --- #

# -- retrieving all -- #
Book.objects.all()
# -- retrieving single -- #
Book.objects.get(id=4)
Book.objects.get(title="Harry Potter")

# ------------------------------------------------------------ #
# --- UPDATING --- #
harry_potter = Book.objects.all()[0]
harry_potter.author = "J.K Rowling"
harry_potter.title = "Harry Potter 1"
harry_potter.save()
# ------------------------------------------------------------ #
# --- DELETING --- #
from book_outlet.models import Book
harry_potter = Book.objects.all()[0]
harry_potter.delete()
