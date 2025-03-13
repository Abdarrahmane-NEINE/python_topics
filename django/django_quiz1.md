
## Django Multiple-Choice and True/False Practice Quiz


### Questions

1. **True or False:** Django is a web framework written in Python.
   - A. True  
   - B. False  
   **Correct Answer:** A. True

2. **Which of the following are valid field types for defining relationships in Django models?** (Select all that apply)
   - A. ForeignKey  
   - B. OneToOneField  
   - C. ManyToManyField  
   - D. MultiValueField  
   **Correct Answers:** A. ForeignKey; B. OneToOneField; C. ManyToManyField

3. **What does a Django view function typically return?**
   - A. A template file  
   - B. An HttpResponse object  
   - C. An HTML string  
   - D. A URL pattern  
   **Correct Answer:** B. An HttpResponse object

4. **True or False:** `MyModel.objects.get(id=1)` returns a QuerySet of matching records.
   - A. True  
   - B. False  
   **Correct Answer:** B. False

5. **True or False:** The DEBUG setting in Django should be set to False in production.
   - A. True  
   - B. False  
   **Correct Answer:** A. True

6. **Which method of a Django Form is used to check if the form data is valid?**
   - A. clean()  
   - B. is_valid()  
   - C. validate()  
   - D. full_clean()  
   **Correct Answer:** B. is_valid()

7. **Which decorator is used to restrict access to a view to only authenticated users?**
   - A. @authenticated  
   - B. @login_required  
   - C. @require_auth  
   - D. @authorized_user  
   **Correct Answer:** B. @login_required

8. **Which command collects all static files into the STATIC_ROOT for deployment?**
   - A. `python manage.py collectstatic`  
   - B. `python manage.py runstatic`  
   - C. `python manage.py gatherstatic`  
   - D. `python manage.py staticfiles`  
   **Correct Answer:** A. `python manage.py collectstatic`

9. **Which of the following are built-in Django middleware classes?** (Select all that apply)
   - A. SecurityMiddleware  
   - B. AuthenticationMiddleware  
   - C. CsrfViewMiddleware  
   - D. LoggingMiddleware  
   **Correct Answers:** A. SecurityMiddleware; B. AuthenticationMiddleware; C. CsrfViewMiddleware

10. **True or False:** If you don’t specify a primary key field, Django will automatically add an id field as the primary key.
   - A. True  
   - B. False  
   **Correct Answer:** A. True

11. **Which syntax is used in a Django template to output the value of a variable named x?**
   - A. `{{ x }}`  
   - B. `{% x %}`  
   - C. `[[ x ]]`  
   - D. `${ x }`  
   **Correct Answer:** A. `{{ x }}`

12. **Which of the following are valid field lookup filters in Django ORM?** (Select all that apply)
   - A. `__exact`  
   - B. `__icontains`  
   - C. `__between`  
   - D. `__lte`  
   **Correct Answers:** A. `__exact`; B. `__icontains`; D. `__lte`

13. **Which of the following are common settings in Django’s `settings.py`?** (Select all that apply)
   - A. INSTALLED_APPS  
   - B. TEMPLATES  
   - C. DATABASES  
   - D. COMPONENTS  
   **Correct Answers:** A. INSTALLED_APPS; B. TEMPLATES; C. DATABASES

14. **True or False:** Django’s built-in authentication system supports permissions and groups for users.
   - A. True  
   - B. False  
   **Correct Answer:** A. True

15. **True or False:** Django REST Framework (DRF) is an official part of Django’s core library.
   - A. True  
   - B. False  
   **Correct Answer:** B. False

16. **What is the purpose of Django’s `include()` function in `urls.py`?**
   - A. To include another URLconf (set of URL patterns) into the project’s URLs  
   - B. To include static files into templates  
   - C. To include views from other frameworks  
   - D. To include query parameters in URLs  
   **Correct Answer:** A. To include another URLconf

17. **Which model field type would you use for a one-to-many relationship?**
   - A. OneToOneField  
   - B. ForeignKey  
   - C. ManyToManyField  
   - D. ManyToOneField  
   **Correct Answer:** B. ForeignKey

18. **Which setting defines the base URL from which user-uploaded media files are served in Django?**
   - A. MEDIA_ROOT  
   - B. MEDIA_URL  
   - C. STATIC_URL  
   - D. MEDIA_PATH  
   **Correct Answer:** B. MEDIA_URL


# Django ORM Interview Questions (Beginner to Intermediate)

## Question 1: Using `select_related` to Avoid N+1 Queries
**Problem:** You have a blog application with an `Author` and a `Book` model. Each `Book` has a foreign key to `Author`. You need to retrieve all books with their author's name while avoiding the N+1 query problem (multiple queries for author data). Write a Django ORM query using `select_related` to fetch books along with their authors in a single query.

**Models:**
```python
class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

**Expected Output:** A Django `QuerySet` of `Book` objects where each book’s `author` field is already fetched from the database. For example:
```python
books = Book.objects.select_related('author').all()
for book in books:
    print(book.title, "-", book.author.name)
```
This should execute **1 query** regardless of the number of books.

Explanation:

Eager Loading: The select_related('author') method tells Django to perform a SQL join between the Book and Author tables. This way, when the query is executed, it retrieves both the book and its associated author in one go.
Single Query: Because the related Author objects are fetched together with the Book objects, no additional queries are triggered when you access book.author.name. This means only one query is sent to the database regardless of the number of books.
Performance: This approach dramatically improves performance, especially when dealing with large datasets, because it avoids the overhead of executing one query per book (which is the essence of the N+1 problem).
Overall, using select_related is a best practice for optimizing queries that involve foreign key relationships, ensuring efficient data retrieval without unnecessary database hits.

### BAD EXAMPLE: This will trigger 1 query to fetch all books and then an additional query for each book to fetch its author.
```python
books = Book.objects.all()
for book in books:
    print(book.title, "-", book.author.name)
```
Explanation:
The initial Book.objects.all() query retrieves all books.
However, because the author field is a foreign key and lazy-loaded by default, each access to book.author.name triggers a separate database query to fetch the related Author object.
This leads to 1 (for books) + N (for each book's author) queries, which is the classic N+1 problem.

### Example usign sql directly rather than ORM 

#### 1. Bad Practice: N+1 Pattern with Raw SQL
In this example, we first query the Book table, then for each book we execute an additional query to fetch the related Author. This mimics the N+1 query problem:

```python
from django.db import connection

cursor = connection.cursor()

# First query: Fetch all books
cursor.execute("SELECT id, title, author_id FROM myapp_book")
books = cursor.fetchall()  # Each row: (id, title, author_id)

for book in books:
    book_id, title, author_id = book
    # For each book, run a query to get the author
    cursor.execute("SELECT name FROM myapp_author WHERE id = %s", [author_id])
    author = cursor.fetchone()  # (name,)
    print(f"{title} - {author[0]}")
```
Explanation:

The first SQL query fetches all books.
Inside the loop, for each book a separate SQL query is executed to retrieve the author.
If there are N books, this will run 1 + N queries, which is inefficient.

#### 2. Good Practice: Single SQL Query Using JOIN
Here, we write one SQL query that joins the Book and Author tables. This retrieves all necessary data in a single query, avoiding the N+1 problem:

```python
from django.db import connection

cursor = connection.cursor()

# Single query using JOIN to fetch book title and author name
sql = """
SELECT b.title, a.name
FROM myapp_book AS b
JOIN myapp_author AS a ON b.author_id = a.id
"""
cursor.execute(sql)
results = cursor.fetchall()  # Each row: (title, author_name)

for title, author_name in results:
    print(f"{title} - {author_name}")
```
Explanation:

The query performs a JOIN between the myapp_book and myapp_author tables.
All the required information is retrieved in one query.
This approach is far more efficient than executing a separate query for each book.

Summary:

Direct SQL Queries: While sometimes necessary, use them judiciously. The ORM is preferred for most use cases.
Avoiding N+1 Problem: Whether using the ORM or raw SQL, aim to structure your queries (e.g., using JOINs) so that related data is fetched in a single query rather than one per record

---

## Question 2: Filtering and Excluding Records
**Problem:** Given an `Employee` model, retrieve all active employees over the age of 30, excluding those who are marked as retired. Use Django ORM filtering (`filter`) and excluding (`exclude`).

**Models:**
```python
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_retired = models.BooleanField(default=False)
```

**Expected Output:** A `QuerySet` of `Employee` objects that meet the criteria.
```python
qs = Employee.objects.filter(is_active=True, age__gt=30).exclude(is_retired=True)
print(list(qs.values_list('name', flat=True)))
```
If employees **Alice** (34, active) and **Bob** (45, active) meet the criteria, while **Charlie** (50, retired) does not, the output would be:
```bash
['Alice', 'Bob']
```

---

## Question 3: Using Annotations and Aggregations
**Problem:** You have `Category` and `Product` models where each `Product` belongs to a `Category`. You want to get the total number of products in each category.

**Models:**
```python
from django.db.models import Count

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
```

**Expected Output:** A `QuerySet` of `Category` objects with an extra field (`product_count`) for the product count:
```python
categories = Category.objects.annotate(product_count=Count('product'))
for cat in categories:
    print(cat.name, cat.product_count)
```
Example output:
```bash
Electronics 5  
Clothing 3
```
**Equivalent SQL**
```sql
SELECT c.name, COUNT(p.id) AS product_count
FROM Category c
LEFT JOIN Product p ON p.category_id = c.id
GROUP BY c.id, c.name;

```

---

## Question 4: Using `Q` and `F` Expressions in Queries
**Problem:** You have a `StoreItem` model representing inventory. You need to:
1. Find all items that are either low in stock (`quantity < reorder_level`) or marked as `urgent_restock`, using a `Q` expression.
2. Increase the quantity of all low-stock items by 10 using an `F` expression (without pulling objects into Python).

**Models:**
```python
from django.db.models import Q, F

class StoreItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    urgent_restock = models.BooleanField(default=False)
```

**Expected Output:**
```python
# Task (a): Find low stock or urgent restock items
low_or_urgent = StoreItem.objects.filter(
    Q(quantity__lt=F('reorder_level')) | Q(urgent_restock=True)
)
```
```python
# Task (b): Increase stock level by 10
StoreItem.objects.filter(quantity__lt=F('reorder_level')).update(quantity=F('quantity') + 10)
```
---

## Question 5: Handling Foreign Key Relationships in Filters
**Problem:** You want to find all books written by authors from the **USA**.

**Expected Output:**
```python
books = Book.objects.filter(author__country="USA")
```
If **Alice** and **Bob** are from the USA and wrote books, only those books will be returned.
```bash
['Django 101', 'Python Tricks']
```

---



**Question:** How can you change the default primary key field type for all new models in a Django project?

**Answer:** By setting `DEFAULT_AUTO_FIELD` in your settings (e.g., `"django.db.models.BigAutoField"`)

**Explanation:** Since Django 3.2, you can specify a default auto field by setting the `DEFAULT_AUTO_FIELD` variable in your project’s settings module.

---

**Question:** If you need to support very large numbers of records, which field should you use instead of `AutoField`?

**Answer:** `BigAutoField`

**Explanation:** `BigAutoField` uses a larger integer type (typically a 64-bit integer) and is suitable for tables with many rows.

---

**Question:** Does Django automatically add an automatic increment field if you define a primary key manually?

**Answer:** No

**Explanation:** If you define a primary key field explicitly in your model, Django will not add another auto-incrementing field.

---

**Question:** In PostgreSQL, what underlying data type is typically used by Django’s `AutoField`?

**Answer:** `SERIAL`

**Explanation:** In PostgreSQL, `AutoField` is generally implemented as a `SERIAL` column, which automatically increments on record insertion.

---

## 10. Django Folder for Project Apps

### 10.1. Organization of Django Apps

#### Introduction
Django projects are usually organized into a main project folder (containing settings, URLs, WSGI/ASGI configuration) and one or more “app” folders. Many developers choose to consolidate all custom apps under an `apps/` directory for clarity, though this isn’t enforced by Django.

#### Questions

**Question:** Is it mandatory to place all your Django apps within a dedicated folder (like `apps/`) in your project?

**Answer:** No

**Explanation:** Django does not enforce a specific folder structure; you may organize your apps as you prefer. However, using an `apps` folder is a common convention for clarity.

---

**Question:** What is the role of the project folder (e.g., `myproject/`) in a Django project structure?

**Answer:** It contains the project settings, URL configuration, and WSGI/ASGI entry points.

**Explanation:** The project folder is the central configuration hub for your Django project, not where individual apps are stored.

---

**Question:** How do you reference an app in the `INSTALLED_APPS` setting if it resides in an `apps/` folder?

**Answer:** By using the Python path (e.g., `"apps.myapp"`)

**Explanation:** Django uses Python import paths; if your app is located in a subfolder named `apps`, you include it as `apps.myapp`.

---

**Question:** What is one benefit of organizing your apps in a dedicated `apps/` folder?

**Answer:** It improves project organization and separation of concerns.

**Explanation:** Grouping apps together can simplify navigation and maintenance in larger projects.

---

**Question:** In a Django project, which file is typically used to run project-wide management commands?

**Answer:** `manage.py`

**Explanation:** The `manage.py` file sits at the project root and is used for running commands such as migrations, testing, and running the development server.


## 11. HTTPResponse Code by Default

### 11.1. Understanding Django’s HttpResponse Default Status Code

#### Introduction
When you create an instance of Django’s `HttpResponse` without specifying a status code, it returns an HTTP `200 OK` by default. This represents a successful response. You can, however, override the status code as needed.

#### Questions

**Question:** What is the default HTTP status code returned by Django’s `HttpResponse` when no status is explicitly provided?

**Answer:** `200 (OK)`

**Explanation:** If no status is set, Django’s `HttpResponse` defaults to `200`, indicating a successful request.

---

**Question:** How can you modify the default HTTP status code in a Django `HttpResponse`?

**Answer:** By passing the `status` parameter to `HttpResponse` (e.g., `HttpResponse("Message", status=201)`).

**Explanation:** The `status` parameter in the `HttpResponse` constructor allows you to customize the response code.

---

**Question:** What would be the effect of returning an `HttpResponse` with `status=204`?

**Answer:** It indicates a “No Content” response, meaning the server successfully processed the request but returns no content.

**Explanation:** HTTP status `204` is used when the server successfully processes a request but does not need to return any content.

---

**Question:** Which Django response subclass is typically used for redirects, and what is its default status code?

**Answer:** `HttpResponseRedirect`, with a default status code of `302`

**Explanation:** `HttpResponseRedirect` is used to send a redirect response and defaults to a `302` status, indicating a temporary redirect.

---

**Question:** If a view returns an `HttpResponse` without any content, what will the client see?

**Answer:** The client will receive an empty body with a `200 OK` status (unless a different status is set).

**Explanation:** An `HttpResponse` without content still sends the HTTP headers; if no content is provided, the body is empty but the status code remains `200` by default.

## 12. Clickjacking Protection Middleware

### 12.1. Django’s XFrameOptionsMiddleware

#### Introduction
Clickjacking is a malicious technique that tricks users into clicking on something different from what they perceive. Django combats this via `XFrameOptionsMiddleware`, which sets HTTP headers (such as `X-Frame-Options`) to control whether a page can be displayed in a frame. Other related security middleware further enhance overall security.

#### Questions

**Question:** What is the primary purpose of Django’s `XFrameOptionsMiddleware`?

**Answer:** To protect against clickjacking by controlling whether a page can be rendered in a frame.

**Explanation:** This middleware adds security headers that instruct browsers to prevent the page from being embedded in frames on other sites.

---

**Question:** Which HTTP header does `XFrameOptionsMiddleware` set by default?

**Answer:** `X-Frame-Options`

**Explanation:** This header specifies whether the browser should allow the page to be framed, and by default, it’s set to prevent framing by external sites.

---

**Question:** How can you configure `XFrameOptionsMiddleware` to allow framing from the same origin?

**Answer:** By setting the `X_FRAME_OPTIONS` setting to `"SAMEORIGIN"`

**Explanation:** `"SAMEORIGIN"` permits the page to be embedded in a frame on the same domain while blocking external domains.

---

**Question:** What is the default value of the `X_FRAME_OPTIONS` setting in Django?

**Answer:** `DENY`

**Explanation:** By default, Django sets `X_FRAME_OPTIONS` to `"DENY"`, which prevents any domain from framing the page.

---

**Question:** Which other security middleware might you use alongside `XFrameOptionsMiddleware` to enhance protection?

**Answer:** `SecurityMiddleware`

**Explanation:** Django’s `SecurityMiddleware` offers additional protections like setting HSTS headers, SSL redirects, and more, complementing clickjacking protection.

## 13. QuerySet.exists()

### 13.1. Efficiently Checking for the Existence of Records

#### Introduction
The `QuerySet.exists()` method is an efficient way to check whether any records match a given `QuerySet` without having to load them all into memory. It returns a boolean value and is particularly useful when you simply need to know if at least one record exists.

#### Questions

**Question:** What does `QuerySet.exists()` return when there is at least one matching record?

**Answer:** `True`

**Explanation:** The method returns `True` if the `QuerySet` contains any records.

---

**Question:** Why is `QuerySet.exists()` generally more efficient than using `len(queryset)` or `queryset.count()`?

**Answer:** It uses a simplified query (typically with `SELECT 1`) and stops once it finds a matching record, reducing database load.

**Explanation:** `exists()` avoids fetching full records or counting all matching rows, which can be expensive for large datasets.

---

**Question:** What does `QuerySet.exists()` return if there are no matching records?

**Answer:** `False`

**Explanation:** If the `QuerySet` is empty, `exists()` returns `False`, indicating that no records were found.

---

**Question:** In what scenario is using `QuerySet.exists()` particularly advantageous?

**Answer:** When you only need to check for the existence of a record (e.g., in conditional logic), not the full data.

**Explanation:** It minimizes database I/O by stopping at the first match, making it more efficient for existence checks.

---

**Question:** If a `QuerySet` has already been evaluated and cached, what does `exists()` do?

**Answer:** It checks the cached results rather than issuing a new database query.

**Explanation:** Once a `QuerySet` is evaluated, `exists()` will use the in-memory cache, which avoids additional database hits.

