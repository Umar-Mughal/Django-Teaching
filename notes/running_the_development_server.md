# Running The Development Server

Django comes with a lightweight web server to run your code quickly. When you run the Django development server, it keeps checking for changes in your code. It reloads automatically, freeing you from manually reloading it after code changes.

Start the development server by typing the following command in the shell prompt:

```shell
python manage.py runserver
```

You can run the Django development server on a custom host and port or tell Django to load a specific
settings file, as follows:

```
python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings
```

> When you have to deal with multiple environments that require different configurations,
> you can create a different settings file for each environment.

This server is only intended for development and is not suitable for production use. To deploy Django
in a production environment, you should run it as a WSGI application using a web server, such as
Apache, Gunicorn, or uWSGI, or as an ASGI application using a server such as Daphne or Uvicorn.
You can find more information on how to deploy Django with different web servers at https://docs.
djangoproject.com/en/4.1/howto/deployment/wsgi/.