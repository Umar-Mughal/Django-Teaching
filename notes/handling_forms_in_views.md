# Handling Forms in Views

Edit the **views.py** file of the blog application and add the following code to it:

```python
from .forms import EmailPostForm

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form})
```

We use the same view both for displaying the initial form and processing the submitted data. The HTTP
**request** method allows us to differentiate whether the form is being submitted. A **GET** request will
indicate that an empty form has to be displayed to the user and a **POST** request will indicate the form
is being submitted. We use **request.method == 'POST'** to differentiate between the two scenarios.

## Form Dispalying & Submission Process

This is the process to display the form and handle the form submission:

- When the page is loaded for the first time, the view receives a **GET** request. In this case, a new **EmailPostForm** instance is created and stored in the **form** variable. This form instance will be used to display the empty form in the template:

```python
form = EmailPostForm()
```

- When the user fills in the form and submits it via **POST**, a form instance is created using the submitted data contained in **request.POST**:

```python
if request.method == 'POST':
  form = EmailPostForm(request.POST)
```

- After this, the data submitted is validated using the form’s **is_valid()** method. This method validates the data introduced in the form and returns **True** if all fields contain valid data. If any field contains invalid data, then **is_valid()** returns **False**. The list of validation errors can be obtained with **form.errors**.


- If the form is not valid, the form is rendered in the template again, including the data submitted and validation errors will be displayed in the template.


- If the form is valid, the validated data is retrieved with **form.cleaned_data**. This attribute is a dictionary of form fields and their values.

We have implemented the view to display the form and handle the form submission. We will now learn how to send emails using Django and then we will add that functionality to the **post_share** view.