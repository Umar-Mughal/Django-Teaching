# Handling ModelForms in Views

For sharing posts by email, we used the same view to display the form and manage its submission. We used the HTTP method to differentiate between both cases; **GET** to display the form and **POST** to submit it. In this case, we will add the comment form to the post detail page, and we will build a separate view to handle the form submission. The new view that processes the form will allow the user to return to the post detail view once the comment has been stored in the database.

## Save Comments

Edit the **views.py** file of the blog application and add the following code:

```python
from .models import Post, Comment
from .forms import CommentForm

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # A comment was posted
    form = CommentForm(request.POST)
    if form.is_valid():
        # Create a comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(request, 'blog/post/comment.html', {
        'post': post,
        'form': form,
        'comment': comment
    })
```

We have defined the **post_comment** view that takes the **request** object and the **post_id** variable as parameters. We will be using this view to manage the post submission. We expect the form to be submitted using the **HTTP** **POST** method. We use the **require_POST** decorator provided by Django to only allow **POST** requests for this view. Django allows you to restrict the **HTTP** methods allowed for views. Django will throw an **HTTP 405** (method not allowed) error if you try to access the view with any other **HTTP** method.

In this view, we have implemented the following actions:

- We retrieve a published post by its **id** using the **get_object_or_404()** shortcut.

- We define a **comment** variable with the initial value **None**. This variable will be used to store the
  comment object when it gets created.

- We instantiate the form using the submitted **POST** data and validate it using the **is_valid()**
  method. If the form is invalid, the template is rendered with the validation errors.

- If the form is valid, we create a new **Comment** object by calling the form’s **save()** method and
  assign it to the **comment** variable, as follows:

  ```python
  comment = form.save(commit=False)
  ```

- The **save()** method creates an instance of the model that the form is linked to and saves it to
  the database. If you call it using **commit=False**, the model instance is created but not saved to
  the database. This allows us to modify the object before finally saving it.

> The save() method is available for ModelForm but not for Form instances since they are not linked to any model.

- We assign the post to the comment we created:

```python
comment.post = post
```

- We save the new comment to the database by calling its **save()** method:

```python
comment.save()
```

- We render the template **blog/post/comment.html**, passing the **post**, **form**, and **comment** objects
  in the template context.

Now let’s create a **URL** pattern for this view.

Edit the **urls.py** file of the **blog** application and add the following **URL** pattern to it:

```python
urlpatterns = [
 	#...
    path('<int:post_id>/comment/', views.post_comment, name="post_comment")
]
```

We have implemented the view to manage the submission of comments and their corresponding URL.

## View Comments & Comment Form

In **post_detail** view retrive the **comments** from database, get **CommentForm** for users to comment and display in the **blog/post/detail.html** template.