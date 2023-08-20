# Adding a Database Index

Let’s define a database index for the publish field. This will improve performance for queries filtering
or ordering results by this field.

```python
class Meta:
  indexes = [
  	models.Index(fields=['-publish'])
  ]
```

We have added the indexes option to the model’s Meta class. This option allows you to define database indexes for your model, which could comprise one or multiple fields, in ascending or descending order, or functional expressions and database functions. We have added an index for the publish field. We use a hyphen before the field name to define the index in descending order. The creation of this index will be included in the database migrations that we will generate later for our blog models.

> Index ordering is not supported on MySQL. If you use MySQL for the database, a descending index will be created as a normal index.

You can read more information about how to define indexes for models at https://docs.djangoproject.
com/en/4.1/ref/models/indexes/.
