# Django Enum: Adding a Status Field

A common functionality for blogs is to save posts as a draft until ready for publication. We will add a status field to our model that will allow us to manage the status of blog posts. We will be using Draft and Published statuses for posts.

```python
class Post(models.Model):
 class Status(models.TextChoices):
   DRAFT = 'DF', 'Draft'
   PUBLISHED = 'PB', 'Published'
 ...
status = models.CharField(max_length=2, choices=Status.choices,default=Status.DRAFT)
```

We have defined the enumeration class Status by subclassing models.TextChoices. The available choices for the post status are DRAFT and PUBLISHED. Their respective values are DF and PB, and their labels or readable names are Draft and Published.

> Django provides enumeration types that you can subclass to define choices simply. These are based on the enum object of Python’s standard library. You can read more about enum at https://docs.python.org/3/library/enum.html
>
> Django enumeration types present some modifications over enum. You can learn about those differences at https://docs.djangoproject.com/en/4.1/ref/models/fields/#enumeration-types.

We can access **Post.Status.choices** to obtain the available choices, **Post.Status.labels** to obtain the human-readable names, and **Post.Status.values** to obtain the actual values of the choices. 

We have also added a new **status** field to the model that is an instance of **CharField**. It includes a **choices** parameter to limit the value of the field to the choices in **Status.choices**. We have also set a default value for the field using the **default** parameter. We use **DRAFT** as the default choice for this field.

> It’s a good practice to define choices inside the model class and use the enumeration types. This will allow you to easily reference choice labels, values, or names from anywhere in your code. You can import the Post model and use Post.Status.DRAFT as a reference for the Draft status anywhere in your code.

Let’s take a look at how to interact with the status choices. 

```python
# Run the following command in the shell prompt to open the Python shell
python manage.py shell
# Then, type the following lines
>>> from blog.models import Post
>>> Post.Status.choices
# You will obtain the enum choices with value-label pairs like this
[('DF', 'Draft'), ('PB', 'Published')]
# Type the following line
>>> Post.Status.labels
# You will get the human-readable names of the enum members as follows
['Draft', 'Published']
# Type the following line
>>> Post.Status.values
# You will get the values of the enum members as follows. These are the values that can be stored in the database for the status field
['DF', 'PB']
# Type the following line
>>> Post.Status.names
# You will get the names of the choices like this
['DRAFT', 'PUBLISHED']
```

You can access a specific lookup enumeration member with Post.Status.PUBLISHED and you can
access its .name and .value properties as well.