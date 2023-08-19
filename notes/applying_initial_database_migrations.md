# Applying initial database migrations

Django applications require a database to store data. The settings.py file contains the database configuration for your project in the DATABASES setting. The default configuration is an SQLite3 database.

SQLite comes bundled with Python 3 and can be used in any of your Python applications. SQLite is
a lightweight database that you can use with Django for development. If you plan to deploy your application in a production environment, you should use a full-featured database, such as PostgreSQL,
MySQL, or Oracle. You can find more information about how to get your database running with Django
at https://docs.djangoproject.com/en/4.1/topics/install/#database-installation.

Your settings.py file also includes a list named INSTALLED_APPS that contains common Django
applications that are added to your project by default. We will go through these applications later in
the Project settings section.

Django applications contain data models that are mapped to database tables. You will create your own
models in the Creating the blog data models section. To complete the project setup, you need to create the tables associated with the models of the default Django applications included in the INSTALLED_APPS setting. 

Django comes with a system that helps you manage database migrations.

Open the shell prompt and run the following commands:

```shell
python manage.py migrate
```

By applying the initial migrations, the tables for the applications listed in the INSTALLED_APPS setting are created in the database.