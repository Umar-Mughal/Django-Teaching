# Activating the Application

We need to activate the blog application in the project, for Django to keep track of the application and be able to create database tables for its models.

Edit the settings.py file and add blog.apps.BlogConfig to the INSTALLED_APPS setting.

```Python
INSTALLED_APPS = [
 ...
 'blog.apps.BlogConfig',
]
```

The BlogConfig class is the application configuration. Now Django knows that the application is active
for this project and will be able to load the application models.

