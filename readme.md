# 1. Django:-

## What is FrameWork ?
- a framework is particual set of rules, ideas, beliefs, which you use in order to deal with problems or to decides what to do.

## What is a Django ?
- Django is a basically a high-lavel python web application framework that enables the rappidly development of web application.
- Open-Source Python Frameworks.
- Follows the model-view-template(MVT) architectual pattern.
- Most popular python framework.

## Why Django ?
- it's fast and simple.
- it's secure.
- it suits any web application project.
- it's well-establised.
- MVT support and object-oriented Apporach.
- Bulit-in Authentication and Authorization.
- Packaging Systems.

## Which companies used in django:-
- Youtube.
- Instagram.
- Disques.
- Spotify.
- The Washington post.
- Bitbucket.
- Drop box.
- Mozila.

# 2. Pre-requisite & Inside the Course:-

## What will learns:-
- Understanding the indentation and syntax the python.
- No prior Django knowledge is required.
- Programming control structures like conditional loops.
- HTML, CSS and Javascript are the fundamental building blocks of web development. Hence is most process good knowledge about it.

## What's inside the course:-
- Setup the understanding django project.
- Working with forms.
- Many small example.
- Urls, Routes, Viwes.
- Class-based viwes.
- A Real-Project (Building a Blog).
- Template & Static Files.
- File Uploads.
- fontend + admin area.
- Data Models & Relationship.
- Session.
- In dept-deployment guide.
- Cookies.
- E-commerce.

# 3. What is Model-View-Template(MVT):-
- The MVT(Model View Template) is a software design pattern.
- It is a collection of three important components Model View and Template.
- Model:- Model is going to act as the interface of your data.
- View:- The View is the user interface -- what you see in your browser when you render a website.
- Template:- A template consists of statics parts of the desired HTML output as we some special syntax describing 
how dynamic content will be inserted.

## Flow Chart to MVT:-
> User  ==>  Django  ==>  URL  ==>  View   ==> Model, Template.

# 4. Install Python, PIP & Django on Windows:-
- first install Python then install django.
- globally install django use command prompt then write pip install django.
- first create the folder then path put then  pip install django.

# 5. How to Create a New Project in Django:-
1. First install Django using command pip install django and check it with django-admin --version.
2. To create a new project, we use command django-admin startproject projectname in terminal.
3. This command creates a main folder with files like manage.py, settings.py, urls.py, and wsgi.py.
4. manage.py is used to run commands like creating apps and running the server.
5. After creating, we run the project using python manage.py runserver to start the development server.

## Available sub-command:-    
> check, compilemessages, createcachetable, dbshell, diffsettings, dumpdata, flush, inspectdb, loaddata, makemessages, makemigrations, migrate, optimizemigration, runserver, sendtestemail, shell, showmigrations, sqlflush, sqlmigrate, sqlsequencereset, squashmigrations, startapp, startproject, test, testserver

## Create Project:-
- pip freeze.
- django-admin startproject mysite.
> command:- django-admin startproject <project-name>.

# 6. How to run Development Server in Django:-
> command:- python manage.py runserver
> PORT input command:- python manage.py runserver <choice-port-number>

# 7. How to Download & Setup Visual Studio Code for Django & Python:-
> install vs code extensions:- django, django template, html & css support, python, python debbuging.

# 8. Folder Structure of a Django Application:-
1. When we run python manage.py startapp appname, it creates an app folder with several default files.
2. It contains models.py for database tables, views.py for logic, admin.py for admin panel, and apps.py for app config.
3. It also has migrations folder which stores database changes and *init*.py which makes the folder a Python package.
4. We need to create urls.py and templates folder manually inside app to manage URLs and HTML files.
5. This structure separates different parts of the app, making the project organized and easy to maintain.

# 9. How to Migrate Default Migrations:-
- sqlite3 data enter.
> commmand:- python manage.py migrate

# 10. How to Install DB Browser for SQLite in Windows? & How to open Data Base?
- Download:- sqlitebrowser.org 
- Version:- DB Browser for SQLite - Standard installer for 64-bit Windows
- http://127.0.0.1:8000/admin

# 11. How to Create Super User in Django:-
> command:- python manage.py createsuperuser
- username:- enter your name (admin, user).
- email:- enter your email.
- password:- enter you choice password. (babu@987)

## 12. What are URLs & Views in Django ? Why to use it?
> URLs(Route):-
- show starting page:- https://www.wscubetech.com/
- Show List of all posts:- https://www.wscubetech.com/blog/
- Show specify posts:- https://www.wscubetech.com/blog/singlepost

> Views:-
- The Logic is executed for different URLs(https method):- 
 Function, Class
- prepare and response data (eg. HTML).

## 13. How to Create URLs ? & Views in Django:-
1. View is a Python function in views.py that takes a request and returns a response.
2. URL is a path in urls.py that maps a browser address to a specific View.
3. We create Views first and then create URL patterns using path() function to connect them.
4. The app's urls.py is included in the project's main urls.py using include().
5. When user opens a URL, Django finds its matching View and executes it to show the output.

## 14. How to Create a Dynamic URL in Django:-
1. Dynamic URL is a URL that can take variable data like id or name in the address itself.
2. It is created using angle brackets < > in path(), like path('student/<int:id>/', views.detail).
3. The variable inside < > is passed as an argument to the connected View function.
4. In View, we receive that variable like def detail(request, id): and use it to fetch data from database.
5. It helps to create one URL pattern for thousands of pages, like /student/1, /student/2 etc.

## 15. Render an HTML Template as Response:-
1. Instead of returning HttpResponse with HTML string, we render a separate HTML file as response.
2. For this, we create a templates folder inside the app and put our HTML files there.
3. In views.py, we use Django's render() function which takes request and template name.
4. Syntax is return render(request, 'index.html') or render(request, 'index.html', {'data': value}) to send data.
5. It separates Python logic from HTML design, making the code clean and manageable.

## 16. Passing Data from a Django View to a Template:-
1. In View function, we create data as a Python dictionary called context, like {'name': 'Rahul'}.
2. This context dictionary is passed as third argument in render() function, e.g. render(request, 'index.html', context).
3. Django sends this context data to the specified HTML template file.
4. Inside the template, we access the data using double curly braces {{ }}, like {{ name }}.
5. This method helps to show dynamic data from Python/database directly on the HTML page.

## 17. How to Use the Django Template for Loop:-
- forloop.counter:- The current Iteration of the loop (1-indexed).
- forloop.counter0:- The current iteration of the loop (0-indexed).
- forloop.revcounter:- The number of iterations from the end of the loop(1-indexed).
- forloop.revcounter0:- The number of iterations from the end of the loop (0-indexed).
- forloop.first:- True if this is the first time through the loop.
- forloop.last:- True if this is the last time through the loop.

## 18. If Else StateMent in Django:-
1. If-Else in Django is used inside the HTML Template to show content based on a condition.
2. It uses template tags, syntax is {% if condition %} ... {% else %} ... {% endif %}.
3. The condition comes from the context data passed by the View, like {% if age > 18 %}.
4. We can also use {% elif %} for multiple conditions check inside the template.
5. It allows us to make dynamic HTML pages that change based on data, like showing login/logout button.

## 19. How to use CSS, JavaScript & Images in Django:-
1. CSS, JS and Images are called Static Files in Django and kept in a static folder inside the app.
2. We have to tell Django about static folder by setting STATIC_URL in settings.py file.
3. In HTML template, first we load static files using tag {% load static %} at the top.
4. Then we link files using syntax like <link rel="stylesheet" href="{% static 'css/style.css' %}">.
5. This method helps Django to manage and serve all design and media files properly.

## 20. Common Header & Footer in Django:-
1. To avoid repeating same header/footer in every page, Django uses template inheritance concept.
2. We create a common file like base.html and put header and footer code inside it.
3. In base.html, we define a block using {% block content %} {% endblock %} where other pages content will come.
4. Other HTML pages extend the base file using {% extends 'base.html' %} and put their content inside the same block.
5. This saves time and if we change header/footer in base file, it changes on all pages automatically.

## 21. How to Use the Extends? Include Django Templates Tag:-
1. Both extends and include are Django template tags used to reuse HTML code.
2. {% extends 'base.html' %} is used for inheritance - child template takes whole structure from base template.
3. While {% include 'header.html' %} is used to insert a small HTML part inside another file.
4. extends uses {% block %} to replace content, but include just copy-pastes the file as it is.
5. We use extends for common layout and include for small reusable parts like header, footer, navbar.

## 22. How to use URL Templates Tags in Django:-
1. URL template tag is used in HTML template to create links dynamically instead of hard-coding URL paths.
2. Syntax is {% url 'url_name' %}, where url_name is the name given in urls.py using name='...'.
3. For dynamic URLs it also passes parameters like {% url 'detail' id=1 %}.
4. If URL path changes in urls.py, we don't need to change it in every template, tag handles it automatically.
5. It makes the project more flexible and avoids broken links when URLs are updated.

## 23. How to Highlight Link in Django:-
1. Highlighting a link means showing which page is currently active, like making the menu bold or different color.
2. In Django, we check current path using request.path inside the template.
3. We use if condition like {% if request.path == '/about/' %} active {% endif %} inside the <a> tag's class.
4. For this, we must enable django.template.context_processors.request in settings.py.
5. When the condition is true, it adds an active CSS class to highlight the current link.

## 24. Http Request Methods in Django:-
> Get Method:-
- The get method sends the encoded information appended to the page request. The page and the encoded information are separated by the ? character.
- Restricted to send upto 1024 characters only.
- Never use GET method if you have password or other sensitive information.
- Cannot be used to send binary data, like images or word documents, to the server.

> Post Method:-
- The POST method transfer information via HTTP headers. The information is encoded as described in case of GET method and put into a header called QUERY_STRING.
- Does not have any restriction on data size to be sent.
- Can be used to send ASCII as well as binary data.
- The data sentr by POST method goes through HTTP header so security depends on HTTP protocol.
- By using Secure HTTP you can make sure that your information is secure.

## 25. How to Implement a form with get method?
1. GET method is used to send form data through the URL as query parameters, like ?name=rahul.
2. In HTML form tag, we set method="GET" and action as the URL where data should be sent.
3. In Django View, we get this data using request.GET.get('field_name').
4. GET method is mainly used for searching, filtering and getting data, not for sensitive info.
5. It is less secure and has character limit, but allows bookmarking and sharing of URL with data.

## 26. Create Form Using Post Method With CSTF Token in Django:-
1. POST method is used to send sensitive data securely through request body, not visible in URL.
2. In HTML form we set method="POST" and must add {% csrf_token %} inside the form tag.
3. CSRF token is a security feature in Django that protects form from Cross-Site Request Forgery attacks.
4. In Django View, data is accessed using request.POST.get('field_name') and we check if request.method == "POST".
5. Without CSRF token, Django will show 403 Forbidden error and will not accept the form data.

## 27. How to Redirect Page in Django:-
> Method 1:- from django.http import HttpResponse,HttpResponseRedirect
> Method 2:- from django.shortcuts import render, redirect

## 28. HTML Form Action Url in Django:-
1. Action attribute in <form> tag tells where the form data should be submitted after clicking submit.
2. In Django, we don't use hard-coded path, we use {% url 'url_name' %} tag inside action, like action="{% url 'submit' %}".
3. The url_name must match the name given in urls.py file.
4. If action is left empty like action="", form data is submitted to the same page URL.
5. Using named URL makes the form flexible, if URL changes in urls.py, form still works without modification.

## 29. Django Form:-
1. Django Form is a built-in class used to create and handle HTML forms easily in Python.
2. We create form class in forms.py file by extending forms.Form or forms.ModelForm.
3. It automatically generates HTML fields, validates user input, and shows error messages.
4. In view, we use form.is_valid() to check data and form.cleaned_data to get cleaned values.
5. It saves time and makes forms more secure compared to manual HTML forms.

## 30. How to Build a Simple Calculator in Django? [Using Html Form]:-
1. Create an HTML form with two number input fields, a select box for operator (+, -, *, /) and method="POST" with CSRF token.
2. Set form action to same view or using {% url 'calculator' %} to submit data.
3. In views.py, get values using request.POST.get() and convert them to int/float.
4. Apply if-else condition based on operator to calculate result and handle divide-by-zero error.
5. Pass the result variable to template using context and display it using {{ result }} in HTML.

## 31. Check Even or Odd Number Using Django:-
1. Create an HTML form with one number input field and POST method with {% csrf_token %}.
2. Submit form data to a Django view using {% url 'evenodd' %} in action attribute.
3. In views.py, get number using request.POST.get() and convert it to integer.
4. Use logic if num % 2 == 0 to check Even, else Odd.
5. Send the result to template through context {'result': result} and display with {{ result }}.