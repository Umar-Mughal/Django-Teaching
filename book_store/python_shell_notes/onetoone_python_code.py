# Creating Address Records
from book_outlet.models import Author, Address
addr1 = Address(street="Some Stree", postal_code="12345", city="London")
addr2 = Address(stree="Some Stree", postal_code="12345", city="New york")
addr1.save()
addr2.save()

# Attaching Address to Author
jkr = Author.objects.get(first_name="J.K")
jkr.address = addr1
jkr.save()

# Getting Author's Address Data
jkr.address
>>> <Address: Address object (1)> # FULL OBJECT
jkr.address.city # GETTING CITY
>>> 'London'
jkr.address.stree # GETTING STREET
>>> 'Some Stree'

# INVERSE

# Getting Address Data of an Author
Address.objects.all()[0].author
>>> <Author: J.K Rowling>
Address.objects.all()[0].author.first_name
>>> 'J.K'
Address.objects.all()[0].author.last_name
>>> 'Rowling'
