# SQL Challenges by Difficulty Level

## Easy Level

### Challenge A: Active Users

#### Scenario:
You maintain a `users` table with a boolean flag indicating whether a user is active. Write a query that returns the names of only the active users (`active = true`), sorted in alphabetical order.

#### Table Schema:
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    active BOOLEAN
);
```

#### Sample Data:
| id | name  | active |
|----|------|--------|
| 1  | Alice | true   |
| 2  | Bob   | false  |
| 3  | Carol | true   |

#### Expected Output:
| name  |
|-------|
| Alice |
| Carol |

#### Solution
```sql
SELECT name 
FROM users 
WHERE active = true
ORDER BY name;
```
---

### Challenge B: Low Stock Products

#### Scenario:
An `inventory` table holds product details, including current stock quantity and a threshold. Write a query that returns the `product_id` and `product_name` for every product where the current quantity is less than its threshold.

#### Table Schema:
```sql
CREATE TABLE inventory (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT,
    quantity INT,
    threshold INT
);
```

#### Sample Data:
| product_id | product_name  | quantity | threshold |
|------------|-------------|----------|-----------|
| 1          | Widget      | 5        | 10        |
| 2          | Gadget      | 15       | 10        |
| 3          | Thingamajig | 8        | 8         |

#### Expected Output:
| product_id | product_name |
|------------|-------------|
| 1          | Widget      |

#### Solution
```sql
SELECT product_id, product_name
FROM inventory 
WHERE quantity < threshold
```

---

## Medium Level

### Challenge C: Total Spent per User

#### Scenario:
You have an `orders` table that tracks each order’s amount along with the user who placed it. Write a query to calculate the total spending per user, but only include users whose total spending is greater than 100. Finally, sort the results in descending order of the total amount spent.

#### Table Schema:
```sql
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT,
    amount NUMERIC,
    order_date DATE
);
```

#### Sample Data:
| order_id | user_id | amount | order_date  |
|----------|--------|--------|------------|
| 1        | 1      | 50     | 2025-01-01 |
| 2        | 1      | 60     | 2025-01-02 |
| 3        | 2      | 80     | 2025-01-03 |
| 4        | 2      | 30     | 2025-01-04 |
| 5        | 3      | 90     | 2025-01-05 |

#### Expected Output:
| user_id | total_amount |
|---------|--------------|
| 1       | 110          |
| 2       | 110          |

**Note:** User 3 is excluded because the total (90) does not exceed 100.

#### Solution
```sql
SELECT user_id, SUM(amount) as total_amount
FROM orders 
GROUP BY user_id
HAVING SUM(amount) > 100
ORDER BY total_amount DESC
```

---

### Challenge D: Department Average Salary

#### Scenario:
An `employees` table contains employee salaries within various departments. Write a query to calculate the average salary for each department, rounded to two decimal places, and then sort the results in descending order by the average salary.

#### Table Schema:
```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary NUMERIC
);
```

#### Sample Data:
| id | name  | department   | salary  |
|----|------|-------------|---------|
| 1  | John  | Sales       | 50000   |
| 2  | Jane  | Sales       | 60000   |
| 3  | Bob   | Engineering | 70000   |
| 4  | Alice | Engineering | 80000   |

#### Expected Output:
| department   | avg_salary |
|-------------|------------|
| Engineering | 75000.00   |
| Sales       | 55000.00   |

#### Solution
```sql
SELECT department, ROUND(AVG(salary), 2) as avg_salary
FROM employees
GROUP BY department
ORDER BY AVG(salary) DESC
```
---

## Hard Level

### Challenge E: Latest Order per User

#### Scenario:
In the `orders` table, each order is associated with a user. Write a query to retrieve the most recent order for each user. Return the `user_id`, `order_id`, and `order_date` of that latest order.

#### Table Schema:
```sql
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT,
    amount NUMERIC,
    order_date DATE
);
```

#### Sample Data:
| order_id | user_id | amount | order_date  |
|----------|--------|--------|------------|
| 1        | 1      | 50     | 2025-01-01 |
| 2        | 1      | 60     | 2025-02-01 |
| 3        | 2      | 70     | 2025-01-15 |
| 4        | 2      | 80     | 2025-02-15 |

#### Expected Output:
| user_id | order_id | order_date  |
|---------|---------|------------|
| 1       | 2       | 2025-02-01 |
| 2       | 4       | 2025-02-15 |

**Hint:** Consider using window functions or a subquery to identify the latest order for each user.
#### Solution
```sql
SELECT o.user_id, o.order_id, o.order_date
FROM orders o
JOIN (
  SELECT user_id, MAX(order_date) AS max_date
  FROM orders
  GROUP BY user_id
) latest ON o.user_id = latest.user_id AND o.order_date = latest.max_date;


-- or
SELECT o.user_id, o.order_id, o.order_date
FROM orders o
WHERE o.order_date = (
  SELECT MAX(o2.order_date)
  FROM orders o2
  WHERE o2.user_id = o.user_id
);

```
