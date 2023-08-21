# Adding a one-to-many Relationship

Posts are always written by an author. We will create a relationship between users and posts that will indicate which user wrote which posts. Django comes with an authentication framework that handles user accounts. The Django authentication framework comes in the **django.contrib.auth** package and contains a **User** model. We will use the **User** model from the Django authentication framework to create a relationship between users and posts.

```python
from django.contrib.auth.models import User
class Post(models.Model):
  author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
```

We have imported the **User** model from the **django.contrib.auth.models** module and we have added an **author** field to the **Post** model. This field defines a **one-to-many** relationship, meaning that each post is written by a user, and a user can write any number of posts. For this field, Django will create a foreign key in the database using the primary key of the related model. 

The **on_delete** parameter specifies the behavior to adopt when the referenced object is deleted. This is not specific to Django; it is an SQL standard. Using **CASCADE**, you specify that when the referenced user is deleted, the database will also delete all related blog posts. You can take a look at all the possible options at https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ForeignKey.on_delete. 

We use **related_name** to specify the name of the reverse relationship, from **User** to **Post**. This will allow us to access related objects easily from a user object by using the **user.blog_posts** notation. We will learn more about this later.

Django comes with different types of fields that you can use to define your models. You can find all field types at https://docs.djangoproject.com/en/4.1/ref/models/fields/. 

The Post model is now complete, and we can now synchronize it to the database. But before that, we need to **activate the blog application** in our Django project.