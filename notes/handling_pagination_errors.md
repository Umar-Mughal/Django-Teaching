# Handling Pagination Errors

Now that the pagination is working, we can add exception handling for pagination errors in the view. The page parameter used by the view to retrieve the given page could potentially be used with wrong values, such as non-existing page numbers or a string value that cannot be used as a page number. We will implement appropriate error handling for those cases.

## EmptyPage Exception

The **Paginator** **object** throws an **EmptyPage** exception when retrieving a non-existing page for instance page 101 because it’s out of range. There are no results to display. 

## PageNotAnInteger Exception

Also Our view should also handle the case when something different than an integer is passed in the page parameter http://127.0.0.1:8000/blog/?page=asdf ,  in this case, the **Paginator object** throws a **PageNotAnInteger** exception when retrieving the page **asdf** because page numbers can only be an integer.

Let’s handle these errorr in our view.

You can learn more about the Paginator class at https://docs.djangoproject.com/en/4.1/ref/paginator/.