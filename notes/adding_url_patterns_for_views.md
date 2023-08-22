# Adding URL Patterns for Views

URL patterns allow you to map URLs to views. A URL pattern is composed of a string pattern, a view, and, optionally, a name that allows you to name the URL project-wide.

Create a **urls.py** file in the directory of the blog application and add the following lines to it:

```python
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name="post_list"),
    path('<int:id>', views.post_detail, name="post_detail")
]
```

In the preceding code, you define an application namespace with the **app_name** variable. This allows you to organize **URLs** by application and use the name when referring to them.

You define two different patterns using the **path()** function. The first URL pattern doesn’t take any arguments and is mapped to the **post_list** view. The second pattern is mapped to the **post_detail** view and takes only one argument id, which matches an integer, set by the path converter int.

## Capturing Value from URL

You use angle brackets to capture the values from the **URL**. Any value specified in the URL pattern as <parameter> is captured as a string. 

You use path converters, such as <int:year>, to specifically match and return an integer. For example <slug:post> would specifically match a slug (a string that can only contain letters, numbers, underscores, or hyphens). You can see all path converters provided by Django at https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters. 

If using path() and converters isn’t sufficient for you, you can use re_path() instead to define complex URL patterns with Python regular expressions. You can learn more about defining URL patterns with regular expressions at https://docs.djangoproject.com/en/4.1/ref/urls/#django.urls.re_path. If you haven’t worked with regular expressions before, you might want to take a look at the Regular Expression HOWTO located at https://docs.python.org/3/howto/regex.html first.

> Creating a urls.py file for each application is the best way to make your applications
> reusable by other projects.

## Include app URL Patterns in Project-Wide URL Patterns

Next, you have to include the URL patterns of the blog application in the main URL patterns of the project. 

Edit the **urls.py** file located in the mysite directory of your project and make it look like the following

```python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
 path('admin/', admin.site.urls),
 path('blog/', include('blog.urls', namespace='blog')),
]
```

The new URL pattern defined with include refers to the URL patterns defined in the **blog** application so that they are included under the blog/ path. You include these patterns under the namespace **blog**.

 Namespaces have to be unique across your entire project. Later, you will refer to your blog URLs easily by using the namespace followed by a colon and the URL name, for example, **blog:post_list** and **blog:post_detail**. You can learn more about URL namespaces at https://docs.djangoproject.com/en/4.1/topics/http/urls/#url-namespaces.