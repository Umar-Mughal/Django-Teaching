# Defining a Default Sort Order

Blog posts are usually displayed in reverse chronological order (from newest to oldest). We will define a default ordering for our model. The default order will apply when obtaining objects from the database when no order is specified in the query.

We have added a Meta class inside the model. This class defines metadata for the model. We use the ordering attribute to tell Django that it should sort results by the publish field. This ordering will apply by default for database queries when no specific order is provided in the query. We indicate descending order by using a hyphen before the field name, -publish. Posts will be returned in reverse chronological order by default.

