# Creating List and Detail Views

Let’s start by creating a view to display the list of posts.

## List View

Edit the **views.py** file of the blog application and make it look like this:

```python
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})
```

This is our very first Django view. The **post_list** view takes the **request** object as the only parameter. This parameter is required by all views.

In this view, we retrieve all the **posts** with the **PUBLISHED** status using the **published** manager that we created previously.

Finally, we use the **render()** shortcut provided by Django to render the list of **posts** with the given template. This function takes the **request** object, the template path, and the context variables to render the given template. It returns an **HttpResponse** object with the rendered text (normally HTML code).

## Detail View

Let’s create a second view to display a single **post**. Add the following function to the **views.py** file:

```python
from django.http import Http404
...
def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found!")

    return render(request, 'blog/post/detail.html', {'post': post})
```

This is the post detail view. This view takes the **id** argument of a post. In the view, we try to retrieve the **Post** object with the given **id** by calling the **get()** method on the custom published manager. We raise an **Http404** exception to return an HTTP 404 error if the model **DoesNotExist** exception is raised, because no result is found. 

Finally, we use the **render()** shortcut to render the retrieved post using a template.