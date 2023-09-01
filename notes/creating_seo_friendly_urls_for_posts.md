# Creating SEO-friendly URLs for Posts

The canonical URL for a blog post detail view currently looks like /blog/1/. We will change the URL pattern to create SEO-friendly URLs for posts. We will be using both the publish date and slug values to build the URLs for single posts. By combining dates, we will make a post detail URL to look like **/blog/2022/1/1/who-was-django-reinhardt/**. We will provide search engines with friendly URLs to index, containing both the title and date of the post.

To retrieve single posts with the combination of publication date and slug, we need to ensure that no post can be stored in the database with the same **slug** and **publish** date as an existing post. We will prevent the **Post** model from storing duplicated posts by defining slugs to be unique for the publication date of the post.

Edit the **models.py** file and add the following **unique_for_date** parameter to the **slug** field of the **Post** model:

```python
class Post(models.Model):
 # ...
 slug = models.SlugField(max_length=250,unique_for_date='publish')
 # ...
```

By using **unique_for_date**, the **slug** field is now required to be unique for the date stored in the **publish** field. Note that the publish field is an instance of DateTimeField, but the check for unique values will be done only against the date (not the time). We have now ensured that slugs are unique for the publication date, so we can now retrieve single posts by the **publish** and **slug** fields.

We have changed our models, so let’s create migrations. Note that **unique_for_date** is not enforced at the database level, so no database migration is required. However, Django uses migrations to keep track of all model changes. We will create a migration just to keep migrations aligned with the current state of the model. 

Run the following commands in the shell prompt:

```Shell
python manage.py makemigrations blog
```

```shell
python manage.py migrate
```

Django will consider that all migrations have been applied and the models are in sync. No action will be done in the database because unique_for_date is not enforced at the database level.