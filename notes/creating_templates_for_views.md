# Creating Templates for Views

## Adding Templates

Let’s add templates to your application to display posts in a user-friendly manner. Create the following directories and files inside your blog application directory:

```
templates/
   blog/
       base.html
       post/
           list.html
           detail.html
```

The preceding structure will be the file structure for your templates. The **base.html** file will include the main HTML structure of the website.

The **list.html** and **detail.html** files will inherit from the **base.html** file to render the blog post list and detail views, respectively.

## Adding Static Files

- create a static directory under blog app on the same level of templates, and add files inside it
- use **{% load static %}** and  **{% static %}** template tag to load static files

