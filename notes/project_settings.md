# Project Settings 

Let’s open the settings.py file and take a look at the configuration of the project. There are several settings that Django includes in this file, but these are only part of all the available Django settings. You can see all the settings and their default values at https://docs.djangoproject.com/en/4.1/ref/settings/. 

Let’s review some of the project settings:

 • DEBUG is a Boolean that turns the debug mode of the project on and off. If it is set to True, Django will display detailed error pages when an uncaught exception is thrown by your application. When you move to a production environment, remember that you have to set it to False. Never deploy a site into production with DEBUG turned on because you will expose sensitive project-related data. 

• ALLOWED_HOSTS is not applied while debug mode is on or when the tests are run. Once you move your site to production and set DEBUG to False, you will have to add your domain/host to this setting to allow it to serve your Django site. 

• INSTALLED_APPS is a setting you will have to edit for all projects. This setting tells Django which applications are active for this site. 

By default, Django includes the following applications:

​	• django.contrib.admin: An administration site 

​	• django.contrib.auth: An authentication framework 

​	• django.contrib.contenttypes: A framework for handling content types

​	• django.contrib.sessions: A session framework 

​	• django.contrib.messages: A messaging framework 

​	• django.contrib.staticfiles: A framework for managing static files

• MIDDLEWARE is a list that contains middleware to be executed. 

• ROOT_URLCONF indicates the Python module where the root URL patterns of your application are defined. 

• DATABASES is a dictionary that contains the settings for all the databases to be used in the project. There must always be a default database. The default configuration uses an SQLite3 database. 

• LANGUAGE_CODE defines the default language code for this Django site. 

• USE_TZ tells Django to activate/deactivate timezone support. Django comes with support for timezone-aware datetimes. This setting is set to True when you create a new project using the startproject management command. 

Don’t worry if you don’t understand much about what you’re seeing here. You will learn more about the different Django settings in the following chapters.