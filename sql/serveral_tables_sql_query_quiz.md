# SQL Challenges by Difficulty Level

## Easy Level

### Challenge 1: Active Users with Order Count
#### Scenario:
You have two tables: one for users and one for orders. List each active user’s name along with the total number of orders they placed. Include users with no orders (show a count of 0).

#### Table Schemas:
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    active BOOLEAN
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT,
    amount NUMERIC,
    order_date DATE
);
```
#### Expected Outcome:
A result set with two columns: the user’s name and their order count. Only active users should be returned.

#### Solution
```sql
SELECT u.name, COALESCE(COUNT(o.order_id), 0) AS total_order
FROM users u
LEFT JOIN orders o ON (o.user_id = u.user_id)
WHERE u.active = true
GROUP BY u.name;
```
---

### Challenge 2: Products and Their Category Names
#### Scenario:
Join the products with their categories to display each product’s name, price, and its category name.

#### Table Schemas:
```sql
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name TEXT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT,
    category_id INT,
    price NUMERIC
);
```
#### Expected Outcome:
A list where each row shows a product name, its price, and the corresponding category name.
#### Solution
```sql
SELECT p.product_name, p.price, c.category_name
FROM products p
JOIN categories c ON p.category_id = c.category_id;

```
---

### Challenge 3: Users and Their Profiles
#### Scenario:
You have separate tables for users and profiles. Return a list of users with their profile information (for example, a short bio). If a user does not have a profile, they should still appear in the result.

#### Table Schemas:
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE profiles (
    profile_id SERIAL PRIMARY KEY,
    user_id INT,
    bio TEXT
);
```
#### Expected Outcome:
Each row should display the user’s name and their bio (or a NULL if no profile exists).
#### Solution
```sql
SELECT u.name, p.bio
FROM users u
LEFT JOIN profiles p ON p.user_id = u.id
```
---

## Medium Level

### Challenge 4: Total Spending per User (With Payment Status)
#### Scenario:
Using three tables—users, orders, and payments—calculate the total amount spent per user. Only consider orders with a corresponding payment record where the status is 'completed'. Return the user’s id, name, and total spent.

#### Table Schemas:
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT,
    amount NUMERIC,
    order_date DATE
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INT,
    status TEXT  -- e.g., 'completed', 'pending'
);
```
#### Expected Outcome:
A result showing each user’s id, name, and sum of order amounts (only for orders with completed payments).
#### Solution
```sql
SELECT u.id, u.name, SUM(o.amount) as total_spent
FROM users u
INNER JOIN orders o ON o.user_id = u.id
INNER JOIN payments p ON (p.order_id = o.order_id AND p.status = 'completed') 
GROUP BY u.id
``` 
---

### Challenge 5: Employee Department Info with Manager Name
#### Scenario:
For each employee, list their name, department name, and their manager’s name (if available). Assume that managers are also stored in the employees table.

#### Table Schemas:
```sql
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name TEXT
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name TEXT,
    department_id INT,
    manager_id INT  -- references employee_id; can be NULL
);
```
#### Expected Outcome:
A list with employee name, department name, and manager name (or NULL if no manager is assigned).
#### Solution
```sql
SELECT e.name, d.department_name, e_m.name
FROM employees e
INNER JOIN department d ON d.department_id = e.department_id
LEFT JOIN employees as e_m ON e_m.id = e.manager_id
```
---

### Challenge 6: Orders with Customer and Product Information
#### Scenario:
Combine orders with customer and product details. For each order, show the order id, customer name, product name, and order date.

#### Table Schemas:
```sql
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name TEXT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT,
    price NUMERIC
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    amount NUMERIC
);
```
#### Expected Outcome:
Rows listing the order id, customer name, product name, and order date for every order.

```sql
SELECT o.order_id,
       c.customer_name,
       p.product_name,
       o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;
```
---

### Challenge 7: Sales Summary by Region
#### Scenario:
Generate a sales summary per region using four tables: orders, customers, products, and regions. For each region, calculate the total sales (sum of order amounts) and the number of orders.

#### Table Schemas:
```sql
CREATE TABLE regions (
    region_id SERIAL PRIMARY KEY,
    region_name TEXT
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name TEXT,
    region_id INT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT,
    category_id INT
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    amount NUMERIC
);
```
#### Expected Outcome:
A result with region name, total sales, and order count, grouped by region. Sort as needed.
```sql
SELECT r.region_name,
       SUM(o.amount) AS total_sales,
       COUNT(o.order_id) AS order_count
FROM regions r
JOIN customers c ON r.region_id = c.region_id
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY r.region_name;
```


### Challenge: Average Items per Order
#### Scenario:
Select all customers who purchased an average of more than 2 items per order. The result should be sorted in ascending order by the average number of items per order.

#### Table Schemas:
```sql
CREATE TABLE Customer (
  customer_id SERIAL PRIMARY KEY,
  name TEXT,
);

CREATE TABLE purchase_order (
  order_id SERIAL PRIMARY KEY,
  customer_id INT REFERENCES Customer(customer_id),
);

CREATE TABLE order_product (
  order_product_id SERIAL PRIMARY KEY,
  order_id INT REFERENCES purchase_order(order_id),
  product_id INT REFERENCES Product(product_id)
);

CREATE TABLE Product (
  product_id SERIAL PRIMARY KEY,
  product_name TEXT,
  price NUMERIC
);
```

#### Expected Query:
This query should return customers who purchased more than an average of 2 items per order, sorted in ascending order of their average item count.
```sql
SELECT 
    c.customer_id,
    c.name,
    AVG(op_count) AS avg_articles
FROM Customer c
JOIN purchase_order o ON c.customer_id = o.customer_id
JOIN (
    SELECT order_id, COUNT(*) AS op_count
    FROM order_product
    GROUP BY order_id
) op ON o.order_id = op.order_id
GROUP BY c.customer_id, c.name
HAVING AVG(op_count) > 2
ORDER BY avg_articles ASC;

```

---

## Hard Level

### Challenge 8: Top Product per Category
#### Scenario:
For each product category, identify the product with the highest total quantity sold. Include the vendor name alongside the product. Use four tables: products, categories, orders, and vendors.

#### Table Schemas:
```sql
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name TEXT
);

CREATE TABLE vendors (
    vendor_id SERIAL PRIMARY KEY,
    vendor_name TEXT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT,
    category_id INT,
    vendor_id INT
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    product_id INT,
    quantity INT,
    order_date DATE
);
```
#### Expected Outcome:
For each category, return the category name, product name, vendor name, and total quantity sold for that product. If there are ties, any one of the top products is acceptable.
#### Solution
```sql
-- SELECT c.category_name, p.name, v.name, SUM(o.quantity) as total_quantity
-- FROM categories c
-- INNER JOIN products p ON c.category_id = p.category_id
-- INNER JOIN vendors v ON v.vendor_id = p.vendor_id
-- INNER JOIN orders o ON o.product_id = p.product_id
-- GROUP BY c.category_id
```
---

### Challenge 9: Employee Performance and Department Hierarchy
#### Scenario:
Using five tables—employees, departments, projects, assignments, and managers—report for each department the department name, manager’s name, and the average hours worked by employees on projects.

#### Table Schemas:
```sql
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name TEXT
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name TEXT,
    department_id INT
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name TEXT,
    department_id INT
);

CREATE TABLE assignments (
    assignment_id SERIAL PRIMARY KEY,
    employee_id INT,
    project_id INT,
    hours_worked NUMERIC
);

CREATE TABLE managers (
    manager_id SERIAL PRIMARY KEY,
    employee_id INT,         -- manager’s employee_id
    department_id INT
);
```
#### Expected Outcome:
For every department, display the department name, the manager’s name, and the average hours worked by its employees on projects. Use appropriate joins and aggregations.