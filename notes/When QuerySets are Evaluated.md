# When QuerySets are Evaluated

Creating a QuerySet doesn’t involve any database activity until it is evaluated. QuerySets usually return another unevaluated QuerySet. You can concatenate as many filters as you like to a QuerySet, and you will not hit the database until the QuerySet is evaluated. When a QuerySet is evaluated, it translates into an SQL query to the database.

QuerySets are only evaluated in the following cases:

- The first time you iterate over them 
- When you slice them, for instance, Post.objects.all()[:3] 
- When you pickle or cache them 
- When you call repr() or len() on them 
- When you explicitly call list() on them 
- When you test them in a statement, such as bool(), or, and, or if