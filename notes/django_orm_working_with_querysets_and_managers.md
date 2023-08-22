# ORM | Working with QuerySets and Managers

Run the following command in the shell prompt to open the Python shell:

```
python manage.py shell
```

## Creating Objects

Type the following lines to create a new object:

```python
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> user = User.objects.get(username='admin')
>>> post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
>>> post.save()
```

Let’s analyze what this code does.

First, we are retrieving the user object with the username admin:

The **get() method** allows you to retrieve a single object from the database. Note that this method expects a result that matches the query. If no results are returned by the database, this method will raise a DoesNotExist exception, and if the database returns more than one result, it will raise a MultipleObjectsReturned exception. Both exceptions are attributes of the model class that the query is being performed on.

Then, we are creating a **Post instance** with a custom title, slug, and body, and set the user that we
previously retrieved as the author of the post.

This object is in memory and not persisted to the database; we created a Python object that can be used during runtime but that is not saved into the database. 

### object.save() Method

Finally, we are saving the Post object to the database using the **save() method**.

The preceding action performs an INSERT SQL statement behind the scenes. We created an object in memory first and then persisted it to the database. 

### Model.manager.create() Method

You can also create the object and persist it into the database in a single operation using the **create() method**, as follows:

```python
Post.objects.create(title='One more post',slug='one-more-post',body='Post body.', author=user)
```

# Updating Objects	

### object.save() Method

Now, change the title of the post to something different and save the object again:

```python
>>> post.title = 'New title'
>>> post.save()
```

This time, the save() method performs an UPDATE SQL statement.

> The changes you make to a model object are not persisted to the database until you call
> the save() method.

# Retrieving Objects

### Model.manager.get() Method

```
user = User.objects.get(username='admin')
```

You already know how to retrieve a single object from the database using the **get()** method. We accessed this method using **User.objects.get()**. Each Django model has at least one manager, and the default manager is called **objects**. You get a QuerySet object using your model manager.

### Model.manager.all() Method

To retrieve all objects from a table, we use the all() method on the default objects manager, like this:

```python
>>> all_posts = Post.objects.all()
```

This is how we create a QuerySet that returns all objects in the database. Note that this QuerySet has not been executed yet. Django QuerySets are lazy, which means they are only evaluated when they are forced to. This behavior makes QuerySets very efficient. If you don’t assign the QuerySet to a variable but instead write it directly on the Python shell, the SQL statement of the QuerySet is executed because you are forcing it to generate output:

```python
>>> Post.objects.all()
<QuerySet [<Post: Who was Django Reinhardt?>, <Post: New title>]>
```

### Model.manager.filter() Method

To filter a QuerySet, you can use the filter() method of the manager. For example, you can retrieve all posts published in the year 2023 using the following QuerySet:

```python
>>> Post.objects.filter(publish__year=2023)
```

You can also filter by multiple fields. For example, you can retrieve all posts published in 2023 by the author with the username admin:

```python
>>> Post.objects.filter(publish__year=2023, author__username='admin')

# This equates to building the same QuerySet chaining multiple filters:

>>> Post.objects.filter(publish__year=2022).filter(author__username='admin')
```

> Queries with field lookup methods are built using two underscores, for example, publish__
> year, but the same notation is also used for accessing fields of related models, such as
> author__username.

### Model.manager.exclude() Method

You can exclude certain results from your QuerySet using the exclude() method of the manager. For example, you can retrieve all posts published in 2023 whose titles don’t start with Why:

```python
>>> Post.objects.filter(publish__year=2023).exclude(title__startswith='Why')
```

### Model.manager.order_by() Method

You can order results by different fields using the order_by() method of the manager. For example, you can retrieve all objects ordered by their title, as follows:

```python
>>> Post.objects.order_by('title')

# Ascending order is implied. You can indicate descending order with a negative sign prefix, like this:

>>> Post.objects.order_by('-title')
```

## Deleting Objects

### object.delete() Method

If you want to delete an object, you can do it from the object instance using the delete() method:

```python
>>> post = Post.objects.get(id=1)
>>> post.delete()
```

> Note that deleting objects will also delete any dependent relationships for ForeignKey objects defined with on_delete set to CASCADE.