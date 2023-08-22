# Using the get_object_or_404 Shortcut

Django provides a shortcut to call **get()** on a given model manager and raises an **Http404** exception instead of a DoesNotExist exception when no object is found.

Edit the **views.py** file to import the get_object_or_404 shortcut and change the post_detail view as follows:

```python
from django.shortcuts import render, get_object_or_404
# ...
def post_detail(request, id):
 post = get_object_or_404(Post,id=id, status=Post.Status.PUBLISHED)
 return render(request,'blog/post/detail.html',{'post': post})
```

In the detail view, we now use the **get_object_or_404()** shortcut to retrieve the desired post. This function retrieves the object that matches the given parameters or an HTTP 404 (not found) exception if no object is found.