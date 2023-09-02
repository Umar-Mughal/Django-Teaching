# Creating Forms from Models | ModelForm

We need to build a form to let users comment on blog posts. Remember that Django has two base classes that can be used to create forms: **Form** and **ModelForm**. We used the **Form** class to allow users to share posts by email. Now we will use **ModelForm** to take advantage of the existing **Comment** model and build a form dynamically for it.

Edit the **forms.py** file of your blog application and add the following lines:

```python
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
```

To create a form from a model, we just indicate which model to build the form for in the **Meta** class of the form. Django will introspect the model and build the corresponding form dynamically.

Each model field type has a corresponding default form field type. The attributes of model fields are taken into account for form validation. By default, Django creates a form field for each field contained in the model. However, we can explicitly tell Django which fields to include in the form using the **fields** attribute or define which fields to exclude using the **exclude** attribute. In the **CommentForm** form, we have explicitly included the **name**, **email**, and **body** fields. These are the only fields that wil be included in the form.

You can find more information about creating forms from models at https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/.