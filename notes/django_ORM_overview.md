# Djagno ORM Overview 

Now that we have a fully functional administration site to manage blog posts, it is a good time to learn how to read and write content to the database programmatically. 

The Django object-relational mapper **(ORM)** is a powerful database abstraction API that lets you create, retrieve, update, and delete objects easily. An ORM allows you to generate SQL queries using the object-oriented paradigm of Python. You can think of it as a way to interact with your database in pythonic fashion instead of writing raw SQL queries. 

The Django ORM is compatible with MySQL, PostgreSQL, SQLite, Oracle, and MariaDB. 

Remember that you can define the database of your project in the DATABASES setting of your project’s settings.py file. Django can work with multiple databases at a time, and you can program database routers to create custom data routing schemes.

Once you have created your data models, Django gives you a free API to interact with them. You can find the data model reference of the official documentation at https://docs.djangoproject.com/en/4.1/ref/models/. 

The Django ORM is based on QuerySets. A QuerySet is a collection of database queries to retrieve objects from your database. You can apply filters to QuerySets to narrow down the query results based on given parameters.