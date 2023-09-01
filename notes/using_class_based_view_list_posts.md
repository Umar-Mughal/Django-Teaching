# Using a Class-Based View to List Posts

To understand how to write class-based views, we will create a new class-based view that is equivalent to the **post_list** view. We will create a class that will inherit from the generic **ListView** view offered by Django. **ListView** allows you to list any type of object.

Edit the **views.py** file of the blog application and add the following code to it:

```python
from django.views.generic import ListView

class PostListView(ListView):
 """
 Alternative post list view
 """
 queryset = Post.published.all()
 context_object_name = 'posts'
 paginate_by = 3
 template_name = 'blog/post/list.html'
```

The **PostListView** view is analogous to the **post_list** view we built previously. We have implemented a class-based view that inherits from the **ListView** class. We have defined a view with the following attributes:

- We use **queryset** to use a **custom** **QuerySet** instead of retrieving all objects. Instead of defining a **queryset** attribute, we could have specified **model = Post** and Django would have built the generic **Post.objects.all()** QuerySet for us.
- We use the context variable **posts** for the query results. The default variable is **object_list** if you don’t specify any **context_object_name**.
- We define the pagination of results with **paginate_by**, returning three objects per page.
- We use a custom template to render the page with **template_name**. If you don’t set a default template, ListView will use blog/post_list.html by default.

Now, edit the **urls.py** file of the blog application and add a new URL pattern using the PostListView class, as follows:

## Pagination in Class-Based Views

In order to keep pagination working, we have to use the right page object that is passed to the template. Django’s **ListView** generic view passes the page requested in a variable called **page_obj**.We have to edit the **post/list.html** template accordingly to include the paginator using the right variable as follows:

```python
{% include "pagination.html" with page=page_obj %}
```

Open http://127.0.0.1:8000/blog/ in your browser and verify that the pagination links work as expected. The behavior of the pagination links should be the same as with the previous **post_list** view. 

The exception handling in this case is a bit different. If you try to load a page out of range or pass a non-integer value in the page parameter, the view will return an HTTP response with the status code **404** (page not found).