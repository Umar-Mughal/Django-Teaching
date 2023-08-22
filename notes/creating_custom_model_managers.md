# Creating Custom Model Managers

The default manager for every model is the **objects** manager. This manager retrieves all the objects in the database. However, we can define custom managers for models. 

Let’s create a custom manager to retrieve all posts that have a **PUBLISHED** status. 

There are two ways to add or customize managers for your models: you can add extra manager methods to an existing manager or create a new manager by modifying the **initial** **QuerySet** that the manager returns. The first method provides you with a **QuerySet** notation like **Post.objects.my_manager()**, and the latter provides you with a **QuerySet** notation like **Post.my_manager.all()**. 

We will choose the second method to implement a manager that will allow us to retrieve posts using the notation **Post.published.all()**. 

Edit the **models.py** file of your blog application to add the custom manager as follows:

```python
class PublishedManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
  # model fields
  # ...
  objects = models.Manager() # The default manager.
  published = PublishedManager() # Our custom manager.
  # ...
```

The first manager declared in a model becomes the default manager. You can use the **Meta** attribute **default_manager_name** to specify a different default manager. If no manager is defined in the model, Django automatically creates the **objects** default manager for it. If you declare any managers for your model, but you want to keep the **objects** manager as well, you have to add it explicitly to your model. In the preceding code, we have added the default **objects** manager and the published custom manager to the **Post** model.

The **get_queryset()** method of a manager returns the **QuerySet** that will be executed. We have overridden this method to build a custom **QuerySet** that filters posts by their status and returns a successive **QuerySet** that only includes posts with the **PUBLISHED** status.

We have now defined a custom manager for the Post model. Let’s test it!	

Start the development server again with the following command in the shell prompt:

```shell
python manage.py shell
```

Now, you can import the **Post** model and retrieve all published posts:

```python
>>> from blog.models import Post
# all published posts
>>> Post.published.all()
# published posts whose title starts with Who
>>> Post.published.filter(title__startswith='Who')
```

