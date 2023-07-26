# Creating a Country Record
from book_outlet.models import Country, Book
germany = Country(name="Germany", code="DE")
germany.save()

# Attaching Country to Book Model
hp1 = Book.objects.all()[0]
hp1.published_countries.add(germany) # special "add" method to link the relation

# Getting Book's Published Countries Data
hp1.published_countries.all() # ALL COUNTRIES WHERE THIS BOOK IS PUBLISHED
>>> <QuerySet [<Country: Country object (1)>]>
hp1.published_countries.all()[0].name
>>> 'Germany'
hp1.published_countries.filter(code='DE') # WHERE CODE IS "DE"
>>> <QuerySet [<Country: Country object (1)>]>

# INVERSE

# Getting Published Country's Books Data
ger = Country.objects.all()[0]
ger.book_set.all()
>>> <QuerySet [<Book: Harry Potter 1 (Rating:5)>]>


