# Django Models

A Django model is a source of information and behaviors of your data. It consists of a Python class that subclasses django.db.models.Model. Each model maps to a single database table, where each attribute of the class represents a database field. When you create a model, Django will provide you with a practical API to query objects in the database easily.

We will define the database models for our blog application. Then, we will generate the database migrations for the models to create the corresponding database tables. When applying the migrations,
Django will create a table for each model defined in the models.py file of the application.