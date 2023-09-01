# Modifying the URL Patterns & Views for Using these SEO-friendly URLs

Let’s modify the URL patterns, view and canonical URL to use the **publication date** and **slug** for the post detail URL.

## URL Patterns

The URL pattern for the post_detail view takes the following arguments: 

- year: Requires an integer 
- month: Requires an integer 
- day: Requires an integer 
- post: Requires a slug (a string that contains only letters, numbers, underscores, or hyphens)

The int **path converter** is used for the **year**, **month**, and **day** parameters, whereas the **slug** path converter is used for the **post** parameter. You learned about path converters in the previous chapter. You can see all path converters provided by Django at https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters.

## View

We will have to change the parameters of the **post_detail** view to match the new URL parameters and use them to retrieve the corresponding **Post** object.

## Canonical URL

We also have to modify the parameters of the canonical URL for blog posts to match the new URL
parameters.

