# Sending Emails with Django

Sending emails with Django is very straightforward. To send emails with Django, you need to have a local **Simple Mail Transfer Protocol (SMTP)** server, or you need to access an external SMTP server,  like your email service provider.

The following settings in **settings.py** allow you to define the SMTP configuration to send emails with Django:

- **EMAIL_HOST**: The SMTP server host; the default is localhost
- **EMAIL_PORT**: The SMTP port; the default is 25
- **EMAIL_HOST_USER**: The username for the SMTP server
- **EMAIL_HOST_PASSWORD**: The password for the SMTP server
- **EMAIL_USE_TLS**: Whether to use a Transport Layer Security (TLS) secure connection
- **EMAIL_USE_SSL**: Whether to use an implicit TLS secure connection

For this example, we will use **Google’s SMTP** server with a standard Gmail account.

If you have a Gmail account, edit the **settings.py** file of your project and add the following code to it:

```python
# Email server configurations
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

Replace your_account@gmail.com with your actual Gmail account. If you don’t have a Gmail account,
you can use the SMTP server configuration of your email service provider.

> Instead of Gmail, you can also use a professional, scalable email service that allows you to send emails via SMTP using your own domain, such as SendGrid (https://sendgrid.com/) or Amazon Simple Email Service (https://aws.amazon.com/ses/). Both services will require you to verify your domain and sender email accounts and will provide you with SMTP credentials to send emails. The Django applications django-sengrid and django-ses simplify the task of adding SendGrid or Amazon SES to your project. You can find installation instructions for django-sengrid at https://github.com/sklarsa/django-sendgrid-v5, and installation instructions for django-ses at https://github.com/django-ses/django-ses.

> If you can’t use an **SMTP** server, you can tell Django to write emails to the console by adding the following setting to the **settings.py** file:
>
> ```python
> EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
> ```
>
> By using this setting, Django will output all emails to the shell instead of sending them. This is very
> useful for testing your application without an SMTP server.

To complete the **Gmail** configuration, we need to enter a password for the **SMTP** server. Since Google uses a two-step verification process and additional security measures, you cannot use your Google account password directly. Instead, Google allows you to create **app-specific** passwords for your account. An **app password** is a 16-digit passcode that gives a less secure app or device permission to access your Google account. So generate a new app and get an **app password**.

Copy the generated **app password**. Edit the **settings.py** file of your project and add the **app password** to the **EMAIL_HOST_PASSWORD** setting.

Then open the python shell (**python manage.py shell**) and execute the following code:

```python
>>> from django.core.mail import send_mail
>>> send_mail('Django mail', 'this email was sent with django', 'sender@gmail.com', ['recepient@gmail.com'], fail_silently=False)
```

The **send_mail()** function takes the **subject**, **message**, **sender**, and list of **recipients** as required arguments. By setting the optional argument **fail_silently=False**, we are telling it to raise an exception
if the email cannot be sent. If the output you see is **1**, then your email was successfully sent.

Check your inbox. You should have received the email.

Now let’s add this functionality to the post_share view.