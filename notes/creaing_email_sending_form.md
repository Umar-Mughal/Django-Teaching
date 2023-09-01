# Creating a Form for Email Sending

First, create a **forms.py** file inside the directory of your blog application and add the following code to it:

```python
from django import forms

class EmailPostForm(forms.Form):
  name = forms.CharField(max_length=25)
  email = forms.EmailField()
  to = forms.EmailField()
  comments = forms.CharField(required=False,widget=forms.Textarea)
```

We have defined our first Django form. The **EmailPostForm** form inherits from the base **Form** class. 

We use different field types to validate data accordingly.

> Forms can reside anywhere in your Django project. The convention is to place them inside a **forms.py** file for each application.

The form contains the following fields: 

- **name**: An instance of **CharField** with a maximum length of 25 characters. We will use it for the name of the person sending the post. 
- **email**: An instance of **EmailField**. We will use the email of the person sending the post recommendation. 
- **to**: An instance of **EmailField**. We will use the email of the recipient, who will receive the email recommending the post recommendation. 
- **comments**: An instance of **CharField**. We will use it for comments to include in the post recommendation email. We have made this field optional by setting required to **False**, and we have specified a custom **widget** to render the field.

## Field Type

Each field type has a default widget that determines how the field is rendered in HTML. The name field is an instance of **CharField**. This type of field is rendered as an <input type="text"> HTML element. The default widget can be overridden with the **widget** attribute. In the comments field, we use the **Textarea** widget to display it as a <textarea> HTML element instead of the default <input> element.

## Field Validation

Field validation also depends on the field type. For example, the **email** and **to** fields are **EmailField** fields. Both fields require a valid email address; the field validation will otherwise raise a **forms. ValidationError** exception and the form will not validate. Other parameters are also taken into account for the form field validation, such as the name field having a maximum length of 25 or the **comments** field being optional.

These are only some of the field types that Django provides for forms. You can find a list of all field types available at https://docs.djangoproject.com/en/4.1/ref/forms/fields/.

