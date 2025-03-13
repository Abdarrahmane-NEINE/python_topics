# Django Interview Question Set

## Beginner Level (Easy)

### 1. (True/False) Django follows the Model-Template-View (MTV) architectural pattern, a variant of MVC.
- True
- False
- **Correct Answer:** True
However, if you have content that you trust and want to render as raw HTML, you can use the |safe filter.
```html
<!-- my_template.html -->
<p>{{ my_html_content|safe }}</p>
```
### 2. (True/False) A single Django project can contain and integrate multiple Django applications.
- True
- False
- **Correct Answer:** True

### 3. (Single Choice) Which file typically contains the database models for a Django app?
- a. models.py
- b. views.py
- c. settings.py
- d. admin.py
- **Correct Answer:** a. models.py

### 4. (Single Choice) What is the correct way to include the content of one template inside another?
- a. `{% include "other_template.html" %}`
- b. `{% import "other_template.html" %}`
- c. `{% insert "other_template.html" %}`
- d. `{% extends "other_template.html" %}`
- **Correct Answer:** a. `{% include "other_template.html" %}`

### 5. (Single Choice) What is the purpose of Django’s manage.py utility?
- a. It defines the models and data schema for the project.
- b. It’s a command-line tool to run tasks like the development server and migrations.
- c. It contains the URL routing configuration for the project.
- d. It is used to configure template loading.
- **Correct Answer:** b. It’s a command-line tool for Django tasks (server, migrations, etc.)

### 6. (True/False) By default, Django’s template system escapes variables to prevent HTML and script injection (XSS).
- True
- False
- **Correct Answer:** True

### 7. (Single Choice) How do you make a model Person appear in the Django admin site?
- a. Add `admin.site.register(Person)` in the app’s admin.py file.
- b. Add `register(Person)` in models.py.
- c. Set `include_in_admin = True` on the Person model.
- d. Nothing — all models are included in admin by default.
- **Correct Answer:** a. Register the model in admin.py with `admin.site.register(Person)`.

### 8. (Single Choice) What argument does HttpResponseRedirect require when used in a view?
- a. The target URL to redirect to (as a string or `reverse()` result).
- b. A view function name.
- c. A template name to render after redirect.
- d. The original HttpRequest object.
- **Correct Answer:** a. A URL string (or resolved URL) to redirect to.

### 9. (True/False) In Django’s settings file, you configure database connections, installed apps, middleware, etc., for your project.
- True
- False
- **Correct Answer:** True

### 10. (Code Snippet) Complete the view code to render an HTML template with context data:
```python
from django.shortcuts import render

def welcome_view(request):
    data = {"user": "Alice"}
    # Return an HTTP response with the rendered template
    return ______________(request, "welcome.html", data)
```
- a. `render(request, "welcome.html", data)`
- b. `HttpResponse("welcome.html", data)`
- c. `include(request, "welcome.html", context=data)`
- d. `redirect("welcome.html", data)`
- **Correct Answer:** a. `render(request, "welcome.html", data)`

---

## Intermediate Level (Moderate)

### 11. (Single Choice) Which template tag is used to extend a base template in Django?
- a. `{% include "base.html" %}`
- b. `{% block "base.html" %}`
- c. `{% extends "base.html" %}`
- d. `{% inherit "base.html" %}`
- **Correct Answer:** c. `{% extends "base.html" %}`

### 12. (Multiple Choice) Which of the following are valid ways to mark strings for translation in Django?
- a. Using `_("Welcome")` in Python code (after importing `gettext` or `ugettext` as `_`).
- b. Using `{% trans "Welcome" %}` in a Django template.
- c. Using `gettext_lazy("Welcome")` in Python code.
- d. Using a fictional `translate("Welcome")` function in Python.
- **Correct Answers:** a, b, c (all of these are correct except the nonexistent `translate()` function)

### 13. (Single Choice) If `Person.objects.get(id=1)` does not find a record, what exception is raised by Django’s ORM?
- a. `Person.DoesNotExist`
- b. `Http404`
- c. `ObjectNotFound`
- d. `PersonNotFoundException`
- **Correct Answer:** a. `Person.DoesNotExist` (each model has its own `DoesNotExist` exception)

### 14. (Multiple Choice) Which of the following will result in a database index being created on a model field?
- a. Setting `db_index=True` on the model field.
- b. Setting `unique=True` on the field.
- c. Adding an `Index` for the field in the model’s `Meta.indexes`.
- d. Including the field in a `unique_together` in the model’s `Meta`.
- e. Setting a field option `index=True` in `Meta` (nonexistent option).
- **Correct Answers:** a, b, c, d (all except e will create an index: unique constraints and explicit indexes create DB indexes)

```python
from django.db import models

class Person(models.Model):
    # a. Using db_index=True creates an index on the 'name' field.
    # Non-unique index for performance (like a standard MySQL index)
    name = models.CharField(max_length=100, db_index=True)

    # b. Setting unique=True creates a unique constraint (and index) on the 'email' field.
     # Unique constraint (creates a unique index)
    email = models.EmailField(unique=True)

    # c. You can add an explicit index via the Meta.indexes option.
    # A non-unique index field
    age = models.IntegerField()

    class Meta:
        # c. This index is explicitly added on the 'age' field.
        # Explicit index for performance on the age field
        indexes = [
            models.Index(fields=['age']),
        ]
        # d. unique_together creates a composite unique constraint (and index) on 'name' and 'email'.
        unique_together = ('name', 'email')
```
### 15. (Single Choice) When should you use `HttpResponseRedirect` instead of a normal `HttpResponse`?
- a. When you need to direct the user’s browser to a different URL (redirect).
- b. When returning HTML content in a response.
- c. When sending JSON data in response to an AJAX call.
- d. When rendering a template with context data.
- **Correct Answer:** a. For redirecting the user to a different URL (`HTTP 302`).

---

## Advanced Level (Hard)

### 16. (Single Choice) Where do you configure the list of middleware that a Django project uses?
- a. In the MIDDLEWARE setting within settings.py.
- b. In the Django app’s apps.py configuration.
- c. In the project’s urls.py file.
- d. In the wsgi.py (or asgi.py) file.
- **Correct Answer:** a. In the MIDDLEWARE list inside settings.py.

### 17. (Multiple Choice) (Old-style) Django middleware can define several processing hooks. Which of these method names are part of the middleware request/response lifecycle?
- a. process_request
- b. process_view
- c. process_response
- d. process_exception
- e. process_body
- **Correct Answer:** a, b, c, d (all except e are valid middleware methods; there is no process_body method)

### 18. (Single Choice) In Django admin, how do you display a custom computed field (e.g. a full name) in the list of objects?
- a. Add the method or property name to the list_display in the model’s ModelAdmin.
- b. Override the admin template to insert the field.
- c. Use list_filter with that field name.
- d. It’s not possible to show custom values in list display.
- **Correct Answer:** a. Include the attribute/method name in list_display of the ModelAdmin.
```python
# models.py
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Custom computed field: full_name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Optional: change the column header in the admin list display
    full_name.short_description = "Full Name"

# admin.py
from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    # a. Include the method name 'full_name' in the list_display
    list_display = ('full_name', 'first_name', 'last_name')

admin.site.register(Person, PersonAdmin)
```
### 19. (Single Choice) What is required at minimum to send an email using Django’s send_mail() function?
- a. Email subject, message body, from_email, and a list of recipient addresses.
- b. A running local SMTP email server.
- c. A pre-configured EmailMessage object.
- d. An active Celery worker for sending emails.
- **Correct Answer:** a. You must provide a subject, message, from-address, and recipient list to send_mail().

### 20. (Code Snippet) In a Django view, you want to retrieve a Person by ID and return a 404 page if it doesn’t exist. Fill in the blank to handle the exception:

```python
from django.http import Http404

def get_person_detail(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        # Person not found: respond with 404
        ________________
    return render(request, "person_detail.html", {"person": person})
```
- a. raise Http404("Person not found")
- b. person = None
- c. return HttpResponse(status=404)
- d. raise Exception("Person not found")
- **Correct Answer:** a. raise Http404("Person not found")

### 21. (True/False) Django’s Paginator class can be used to split a QuerySet or list into pages of a fixed size.
   True
   False
- **Correct Answer:** True

### 22. (Single Choice) Which manage.py command creates new migration files based on model changes?
- a. python manage.py makemigrations
- b. python manage.py migrate
- c. python manage.py createMigration
- d. python manage.py schema
- **Correct Answer:** a. python manage.py makemigrations

### 23. (Single Choice) After adding new translation strings in your code and generating message files, which command should you run to compile the translations for use?
- a. python manage.py compilemessages
- b. python manage.py makemessages --compile
- c. django-admin compiletranslations
- d. python manage.py translate
- **Correct Answer:** a. python manage.py compilemessages

### 24. (Single Choice) What HTTP status code does a Django HttpResponseRedirect return by default?
- a. 301 (Moved Permanently)
- b. 302 (Found)
- c. 404 (Not Found)
- d. 500 (Server Error)
- **Correct Answer:** b. 302 (a standard redirect status)

### 25. (Code Snippet) Using Django’s paginator, fill in the blank to get the total number of pages:

```python
from django.core.paginator import Paginator

items = list(range(1, 101))   # 100 items
paginator = Paginator(items, 10)  # 10 items per page
first_page = paginator.page(1)
# Total number of pages in the paginator:
total_pages = paginator.________
```
- a. count
- b. num_pages
- c. page_count
- d. total_items
- **Correct Answer:** b. num_pages

### 26. (Single Choice) Which management command gathers all static files into the directory specified by STATIC_ROOT (for production deployment)?
- a. python manage.py collectstatic
- b. python manage.py getstatic
- c. python manage.py exportstatic
- d. python manage.py gatherfiles
- **Correct Answer:** a. python manage.py collectstatic

### 27. (Multiple Choice) Which of the following are generic class-based views provided by Django out of the box?
- a. ListView
- b. DeleteView
- c. FormView
- d. TableView
- **Correct Answer:** a, b, c (ListView, DeleteView, and FormView are built-in generic views; TableView does not exist)

### 28. (Single Choice) What is the key difference between select_related and prefetch_related in Django’s ORM?
- a. select_related performs a SQL join to include related model data (for ForeignKey/OneToOne), while prefetch_related performs separate queries (suited for ManyToMany or reverse ForeignKey relations).
- b. There is no difference; they are aliases of each other.
- c. select_related is used for large datasets, prefetch_related for small ones.
- d. select_related works only with Django Rest Framework, prefetch_related is in Django ORM.
- **Correct Answer:** a. select_related uses SQL joins for single-valued relations; prefetch_related uses additional queries for multi-valued relations.

### 29. (Single Choice) Which exception class can you raise in a Django view to immediately return a 403 Forbidden HTTP response?
- a. PermissionDenied
- b. Http404
- c. BadRequest
- d. SuspiciousOperation
- **Correct Answer:** a. PermissionDenied (raising this will result in a 403 response)

### 30. (Multiple Choice) In Django’s admin, which of these options can you set in a ModelAdmin to customize how a model is displayed?
 - a. list_display
 - b. search_fields
 - c. list_filter
 - d. ordering
 - e. form_fields
 - **Correct Answer:** a, b, c, d (there is no form_fields option; use fields or fieldsets to control form fields)
```python
# models.py
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# admin.py
from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    # a. list_display: Fields to display in the admin list view
    list_display = ('first_name', 'last_name', 'email')
    
    # b. search_fields: Fields to search against in the admin
    search_fields = ('first_name', 'last_name', 'email')
    
    # c. list_filter: Fields to filter the list view
    list_filter = ('last_name',)
    
    # d. ordering: Default ordering for the admin list view
    ordering = ('first_name',)

admin.site.register(Person, PersonAdmin)
```
### 31. (Multiple Choice) Django provides several built-in email-sending utilities. Which of the following functions are provided by Django’s email module?
 - a. django.core.mail.send_mail
 - b. django.core.mail.send_mass_mail
 - c. django.core.mail.mail_admins
 - d. django.core.mail.mail_managers
 - e. django.core.mail.send_html_mail
 - **Correct Answer:** a, b, c, d (there is no built-in send_html_mail function)

### 32. (Single Choice) Which manage.py command is used to extract translation strings from your code into new or updated .po files?
 - a. python manage.py makemessages
 - b. python manage.py compilemessages
 - c. python manage.py extractmessages
 - d. python manage.py maketranslations
 - **Correct Answer:** a. python manage.py makemessages

### 33. (Single Choice) When should you use django.utils.translation.gettext_lazy (a.k.a. ugettext_lazy) instead of gettext?
 - a. When marking strings for translation at import time (e.g. in module-level constants, model field verbose_names) so that actual translation is deferred.
 - b. When translating strings inside a view or function right before rendering to the user.
 - c. Only when the text is very long or infrequently used.
 - d. When you want to support lazy database queries.
 - **Correct Answer:** a. Use the lazy variant for module-level or model-level translatable strings that should be evaluated in the user’s locale later.

### 34. (Code Snippet) In a Django model definition, fill in the blank with the appropriate translation function for a field’s verbose name:
```python
from django.utils.translation import ______ as _

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    # ... other fields ...
```
 - a. gettext
 - b. gettext_lazy
 - c. get_text
 - d. ugettext
 - **Correct Answer:** b. gettext_lazy (imported as _ for use in model field definitions)

### 35. (Multiple Choice) Which statements are true about Django middleware execution order?
 - a. Middleware listed first in settings.MIDDLEWARE is called first during the request phase.
 - b. Middleware listed last in settings.MIDDLEWARE is called first during the response phase.
 - c. A middleware can short-circuit the request/response cycle by returning an HttpResponse in the request phase, skipping later middleware and the view.
 - d. The order of middleware in settings.py does not matter.
 - **Correct Answer:** a, b, c (middleware order does matter; the last option is false)

### 36. (Code Snippet) You are writing a middleware to block certain user agents. Fill in the blank to return an HTTP 403 Forbidden response when a bad bot is detected:
```python
from django.http import HttpResponseForbidden

class BlockBadBotMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the User-Agent contains "EvilBot", block the request
        if "EvilBot" in request.META.get('HTTP_USER_AGENT', ''):
            ________________
        return self.get_response(request)
```
 - a. return HttpResponseForbidden("Forbidden")
 - b. raise PermissionDenied
 - c. return HttpResponse(status=403)
 - d. request.META['blocked'] = True
 - **Correct Answer:** a. return HttpResponseForbidden("Forbidden")

### 37. (Single Choice) How do you specify a custom user model for a Django project (to override the default auth.User)?
 - a. Set the AUTH_USER_MODEL setting to <app_name>.<ModelName> for your custom user model.
 - b. Add your user model class to INSTALLED_APPS.
 - c. Replace the import of django.contrib.auth.models.User everywhere with your model.
 - d. You cannot change the user model in Django.
 - **Correct Answer:** a. Configure AUTH_USER_MODEL in settings with "yourapp.YourUserModel".

### 38. (Single Choice) How can you set a default ordering for a Django model’s QuerySet (so that queries are ordered unless explicitly overridden)?
 - a. Define an ordering list/tuple inside the model’s Meta class.
 - b. Use order_by() on every QuerySet in your code.
 - c. Set a class attribute default_order on the model.
 - d. It’s not possible to set a default sort order in the model definition.
 - **Correct Answer:** a. Add ordering = [...] in the model’s Meta to set a default sort order.
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # a. The default ordering is set here: by 'price' in ascending order.
        ordering = ['price']

    def __str__(self):
        return self.name
```

### 39. (Single Choice) What decorator can be used to ensure that only authenticated users can access a particular view?
 - a. login_required
 - b. require_POST
 - c. user_passes_test
 - d. staff_member_required
 - **Correct Answer:** a. @login_required

### 40. (Code Snippet) Using Django’s Q objects for complex queries: fill in the blank to query for persons named either John or Jane.
```python
from django.db.models import Q

# Filter Person objects where first_name is "John" OR first_name is "Jane"
people = Person.objects.filter( Q(first_name="John") ___ Q(first_name="Jane") )
```
 - a. | (bitwise OR operator)
 - b. & (ampersand, for AND)
 - c. + (plus sign)
 - d. , (comma)
 - **Correct Answer:** a. | (use the OR operator between Q clauses)

