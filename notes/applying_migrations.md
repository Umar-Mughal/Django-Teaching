# Applying Migrations

Let’s sync the database with the new model.

Execute the following command in the shell prompt to apply existing migrations:

```shell
python manage.py migrate
```

You will get an output that ends with the following line:

```shell
Applying blog.0001_initial... OK
```

We just applied migrations for the applications listed in **INSTALLED_APPS**, including the blog application. After applying the migrations, the database reflects the current status of the models. 

If you edit the **models.py** file in order to add, remove, or change the fields of existing models, or if you add new models, you will have to create a new migration using the **makemigrations command**. Each migration allows Django to keep track of model changes. Then, you will have to apply the migration using the **migrate command** to keep the database in sync with your models.