# Getting All Books where Author's last_name is "Rowling"
books_by_rowling = Book.objects.filter(author__last_name="Rowling")
books_by_rowling
>>> <QuerySet [<Book: Harry Potter 1 (Rating:5)>]>

# Getting All Books where Author's last_name contains "wling"
books_by_rowling = Book.objects.filter(author__last_name__contains="wling")
books_by_rowling
>>> <QuerySet [<Book: Harry Potter 1 (Rating:5)>]>

