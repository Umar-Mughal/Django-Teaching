# Creating and Applying Migrations

## Creating Migration

Now that we have a data model for blog posts, we need to create the corresponding database table. Django comes with a **migration system** that tracks the changes made to models and enables them to propagate into the database. 

The **migrate command** applies migrations for all applications listed in **INSTALLED_APPS**. It synchronizes the database with the current models and existing migrations. 

First, we will need to create an initial migration for our **Post model**. 

Run the following command in the shell prompt from the root directory of your project:

```shell
python manage.py makemigrations blog
```

Django just created the **0001_initial.py** file inside the **migrations directory** of the blog application. This migration contains the SQL statements to create the database table for the **Post model** and the definition of the **database index** for the publish field.

You can take a look at the file contents to see how the migration is defined. A migration specifies dependencies on other migrations and operations.

## Inspecting Migration

Let’s take a look at the SQL code that Django will execute in the database to create the table for your model. The **sqlmigrate command** takes the migration names and returns their SQL without executing it. 

Run the following command from the shell prompt to inspect the SQL output of your first migration:

```shell
python manage.py sqlmigrate blog 0001
```

The output should look as follows:

```sql
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(250) NOT NULL, "slug" varchar(250) NOT NULL, "body" text NOT NULL, "publish" datetime NOT NULL, "created" datetime NOT NULL, "updated" datetime NOT NULL, "status" varchar(2) NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
CREATE INDEX "blog_post_publish_bb7600_idx" ON "blog_post" ("publish" DESC);
COMMIT;
```

The exact output depends on the database you are using. The preceding output is generated for SQLite.

As you can see in the output,Django generates the table names by combining the application name and the lowercase name of the model (**blog_post**), but you can also specify a custom database name for your model in the Meta class of the model using the **db_table** attribute.

Django creates an auto-incremental **id column** used as the **primary key** for each model, but you can also override this by specifying **primary_key=True** on one of your model fields. The default id column consists of an integer that is incremented automatically.

The following three database indexes are created: 

- An index with descending order on the **publish column**. This is the index we explicitly defined with 				the **indexes option** of the model’s Meta class. 
- An index on the **slug column** because SlugField fields imply an index by default. 
- An index on the **author_id** column because ForeignKey fields imply an index by default.

## Comparison Model to DB Table

Let’s compare the Post model with its corresponding database blog_post table:

![model_to_db_comparison](media/model_to_db_comparison.png)

Figure 1.5 shows how the model fields correspond to database table columns.

