# Class Based Views

We have built the blog application using function-based views. Function-based views are simple and powerful, but Django also allows you to build views using classes. 

Class-based views are an alternative way to implement views as Python **objects** instead of functions. Since a view is a function that takes a web request and returns a web response, you can also define your views as class methods. Django provides base view classes that you can use to implement your own views. All of them inherit from the **View** class, which handles HTTP method dispatching and other common functionalities.

## Why use class-based views

Class-based views offer some advantages over function-based views that are useful for specific use cases. Class-based views allow you to: 

- Organize code related to HTTP methods, such as **GET**, **POST**, or **PUT**, in separate methods, instead of using conditional branching
- Use multiple inheritance to create reusable view classes (also known as mixins)

