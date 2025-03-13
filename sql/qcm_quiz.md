# SQL Interview Practice Quiz (Codingame Style)

### Beginner Level (10 Questions)

**True/False:** By default, the ORDER BY clause will sort the results in descending order if no sort direction is specified.

**Answer:** False.

**Explanation:** If you don’t specify ASC or DESC, ORDER BY sorts in ascending order by default (from smallest to largest). You need to add DESC explicitly to sort in descending order.

---

**Select the correct answer:** Which SQL keyword is used to eliminate duplicate rows from a result set?

A. UNIQUE  
B. ONLY  
C. DISTINCT  
D. SINGLE  

**Answer:** C. DISTINCT.

**Explanation:** DISTINCT is placed right after SELECT to return only unique values. (Option A, "UNIQUE", is not a valid SELECT keyword in standard SQL; DISTINCT is the correct keyword to remove duplicates.)

---

**Select the correct answer:** Which clause is used to filter the rows returned by a SELECT query based on a specified condition?

A. SELECT  
B. WHERE  
C. ORDER BY  
D. GROUP BY  

**Answer:** B. WHERE.

**Explanation:** The WHERE clause filters rows by a condition. SELECT chooses columns, GROUP BY groups rows, and ORDER BY sorts the result – none of those filter rows like WHERE does.

---

**True/False:** An INNER JOIN will return only the rows that have matching values in both of the joined tables.

**Answer:** True.

**Explanation:** By definition, an inner join yields only the matching rows between the two tables based on the join condition. Rows that don’t find a match in the other table are excluded from the result.

---

**Multiple correct answers:** Which of the following are aggregate functions in SQL? (Select all that apply.)

A. COUNT()  
B. SUM()  
C. WHERE  
D. AVG()  

**Answer:** A, B, and D. (COUNT(), SUM(), and AVG() are aggregate functions.)

**Explanation:** Aggregate functions perform a calculation on multiple rows and return a single value. COUNT(), SUM(), AVG(), as well as MIN() and MAX(), are common aggregate functions. WHERE is not a function at all – it’s a clause used for filtering rows.

---

**Complete the SQL code:** Fill in the missing part of the query to count all rows in a table named Orders.

```sql
SELECT ________
FROM Orders;
```

**Answer:**

```sql
SELECT COUNT(*)
FROM Orders;
```

**Explanation:** COUNT(*) returns the number of rows in the table (including rows with NULL values). This query will output a single number representing the total count of records in Orders.

---

**Correct the SQL code:** The query below attempts to show each department and the average salary in that department, but it errors out. Fix the query.

```sql
SELECT department, AVG(salary)
FROM Employees;
```

**Answer:**

```sql
SELECT department, AVG(salary)
FROM Employees
GROUP BY department;
```

**Explanation:** When using an aggregate function like AVG() alongside a non-aggregated column (department), you must group the results by that column. The GROUP BY department clause ensures the average salary is calculated for each department.

---

**Select the correct answer:** Which SQL operator is used in a WHERE clause for pattern matching (such as finding names that start with "A")?

A. LIKE  
B. PATTERN  
C. CONTAINS  
D. FIND  

**Answer:** A. LIKE.

**Explanation:** The LIKE operator is used with wildcards (for example, WHERE name LIKE 'A%') to match string patterns. (Options B, C, D are not valid SQL pattern-matching operators in standard SQL.)

---

**Select the correct answer:** Which keyword is used to assign a temporary name (alias) to a column or table in a SQL query?

A. AS  
B. ALIAS  
C. RENAME  
D. = (equals sign)  

**Answer:** A. AS.

**Explanation:** You use AS to give a column or table an alias. For example: SELECT column_name AS alias_name FROM table AS alias_name. (The keyword AS is optional in some SQL dialects, but it improves readability. Other options listed are not used for this purpose in a SELECT query.)

---

**Select the correct answer:** Which clause is used to sort the results of a query?

A. SORT BY  
B. ORDER  
C. ORDER BY  
D. GROUP BY  

**Answer:** C. ORDER BY.

**Explanation:** ORDER BY is the clause that sorts the result set either in ascending or descending order. (There is no SORT BY clause in SQL. GROUP BY groups results and ORDER by itself is incomplete syntax.) By default, ORDER BY sorts in ascending order; use DESC to sort in descending order.

### Intermediate Level (10 Questions)

**True/False:** The UNION ALL operator will eliminate any duplicate rows from the combined result of two SELECT queries.

**Answer:** False.

**Explanation:** UNION ALL does not remove duplicates; it simply appends the results of the second query to the first, keeping all rows. In contrast, the plain UNION (without ALL) will eliminate duplicate rows from the combined results.

---

**True/False:** In SQL, the condition NULL = NULL evaluates to TRUE.

**Answer:** False.

**Explanation:** In SQL, NULL represents an unknown value. Any comparison to NULL (e.g., NULL = NULL) yields NULL/False (treated as UNKNOWN) rather than true. To check for NULL values, you must use IS NULL or IS NOT NULL (for example, column IS NULL).

---

**Select the correct answer:** Which type of JOIN returns all rows from the left table and only the matching rows from the right table?

A. INNER JOIN  
B. LEFT JOIN  
C. RIGHT JOIN  
D. FULL JOIN  

**Answer:** B. LEFT JOIN.

**Explanation:** A LEFT JOIN (left outer join) returns all rows from the left table, and the matching rows from the right table. If there’s no match for a left-table row, the result will have that row with NULLs for the right-table columns. (A RIGHT JOIN does the opposite, and a FULL JOIN returns all rows from both tables.)

---

**Select the correct answer:** Which operator can be used in a WHERE clause to filter rows based on a list of values returned by a subquery?

A. EXISTS  
B. IN  
C. = (equals)  
D. LIKE  

**Answer:** B. IN.

**Explanation:** The IN operator is used to compare a value to a list of values. For example: WHERE department_id IN (SELECT id FROM Departments ...). This checks if a value is among those returned by the subquery. (EXISTS is used differently – it checks for the existence of any row from a subquery, not to match a specific value against a list.)

---

**Select the correct answer:** Which clause is used to filter grouped results after a GROUP BY has been applied?

A. WHERE  
B. HAVING  
C. GROUP BY  
D. FILTER  

**Answer:** B. HAVING.

**Explanation:** The HAVING clause filters groups after aggregation. For example, you would use HAVING COUNT(*) > 5 to restrict results to groups that satisfy that condition. You cannot use WHERE for conditions on aggregated values, because WHERE filters rows before grouping.

---

**Multiple correct answers:** What are potential effects of adding an index on a column in a database table? (Select all that apply.)

A. Faster SELECT queries when filtering on that column.  
B. Slower INSERT and UPDATE operations on that table.  
C. Reduced storage space usage.  
D. Additional storage space usage.  

**Answer:** A, B, and D.

**Explanation:** An index can significantly speed up SELECT queries that filter or join on the indexed column (option A). However, indexes incur overhead: whenever you insert or update rows, the index must be updated, which can slow down write operations (option B). Indexes also occupy extra storage, increasing the database size (option D). (Option C is incorrect—indexes use extra space, they do not reduce storage usage.)

---

**Complete the SQL code:** Fill in the missing part of this query to list all employees who have a salary higher than the average salary of all employees.

```sql
SELECT name, salary
FROM Employees
WHERE salary > (SELECT __________(salary) FROM Employees);
```

**Answer:**

```sql
SELECT name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
```

**Explanation:** The subquery SELECT AVG(salary) FROM Employees computes the average salary of all employees. The outer query then selects those employees whose salary is greater than that average. We use the aggregate function AVG() inside the subquery.

---

**Correct the SQL code:** The query below is intended to find departments with more than 5 employees, but it has an error. Fix the query.

```sql
SELECT department, COUNT(*)
FROM Employees
WHERE COUNT(*) > 5
GROUP BY department;
```

**Answer:**

```sql
SELECT department, COUNT(*)
FROM Employees
GROUP BY department
HAVING COUNT(*) > 5;
```

**Explanation:** You cannot use an aggregate (COUNT(*)) in the WHERE clause. The correct approach is to use a HAVING clause to filter groups after the GROUP BY. Here, HAVING COUNT(*) > 5 ensures only departments with more than 5 employees appear in the results.

---

**True/False:** A self join is a join in which a table is joined with itself.

**Answer:** True.

**Explanation:** In a self join, a table is joined to itself as if it were two separate tables. Typically you use table aliases to differentiate the two references to the same table. Self joins are useful for comparing rows in a table to other rows in the same table (for example, an employee table joined to itself to compare employees with their managers).

---

**True/False:** You can use a column alias defined in the SELECT clause in the WHERE clause of the same query.

**Answer:** False.

**Explanation:** SQL does not allow using a SELECT list alias in the WHERE clause because the WHERE is evaluated before the SELECT clause. If you need to reuse an expression, you can either repeat the expression in the WHERE clause or use a subquery or Common Table Expression to define it earlier. (One exception: you can use aliases in the ORDER BY clause, since ORDER BY happens after SELECT.)


### Advanced Level (10 Questions)

**True/False:** A correlated subquery is executed once for each row of the outer query.

**Answer:** True.

**Explanation:** A correlated subquery is a subquery that refers to columns from the outer query. Because it depends on each row of the outer query, the subquery runs repeatedly — for each row of the outer result. This can be less efficient than a regular (non-correlated) subquery, which runs just once and returns a result used by the outer query.

---

**Select the correct answer:** Which keyword is used to start a Common Table Expression (CTE) in SQL?

A. WITH  
B. AS  
C. CTE  
D. BEGIN  

**Answer:** A. WITH.

**Explanation:** A CTE begins with the WITH keyword. For example:

```sql
WITH Summary AS (SELECT ... FROM ... )
SELECT * FROM Summary;
```

Inside the parentheses after an alias (here Summary), you put the subquery definition. (AS is used inside the CTE syntax to link the name to the subquery, but the whole CTE starts with WITH.)

---

**True/False:** A FULL OUTER JOIN returns all rows from both tables, matching rows where the join condition is met and using NULLs for missing matches.

**Answer:** True.

**Explanation:** A full outer join combines the results of a left and right join: it returns every row from both tables. Where a match exists between the tables, you get one combined row. Where a row from one side has no match on the other, the result will include that row with NULL values for the other table’s columns.

---

**True/False:** If a ROLLBACK is executed inside a transaction, all changes made in that transaction are undone.

**Answer:** True.

**Explanation:** A ROLLBACK will revert all modifications made during the current transaction, restoring the data to its state before the transaction began. In transactional SQL, COMMIT permanently saves changes, whereas ROLLBACK discards them, maintaining the atomicity of transactions (all-or-nothing).

---

**Multiple correct answers:** Which of the following statements are true about stored procedures in SQL? (Select all that apply.)

A. Stored procedures allow you to encapsulate and reuse SQL logic by calling the procedure by name.  
B. Stored procedures cannot accept parameters.  
C. Stored procedures execute on the database server, not the client.  
D. Stored procedures always return a value.  

**Answer:** A and C.

**Explanation:** Stored procedures are reusable server-side routines that can encapsulate complex SQL logic (option A is true, they promote reusability, and can be called by name). They typically run on the database server (option C true), which can reduce network overhead. They can accept parameters (so option B is false). And they do not always return a value (option D is false) – unlike functions, procedures might simply perform actions (though they can return output via OUT parameters or SELECTs if designed to).

---

**Select the correct answer:** In a window function, which clause is used inside the OVER(...) to divide the result set into subsets (partitions) for calculation?

A. GROUP BY  
B. PARTITION BY  
C. DIVIDE BY  
D. ORDER BY  

**Answer:** B. PARTITION BY.

**Explanation:** The PARTITION BY clause within OVER(...) splits the result set into partitions (subgroups) for the window function to operate on. For example, `AVG(salary) OVER (PARTITION BY department)` will compute an average salary per department without collapsing rows. (ORDER BY inside OVER defines ordering within each partition, and is not used for partitioning the data itself.)

---

**Select the correct answer:** Which SQL command can be used to display the execution plan for a query in many relational database systems?

A. EXPLAIN  
B. DESCRIBE PLAN  
C. EXECUTE PLAN  
D. ANALYZE QUERY  

**Answer:** A. EXPLAIN.

**Explanation:** The EXPLAIN command (and vendor-specific equivalents like EXPLAIN PLAN or using GUI tools) shows the query execution plan. The execution plan details how the database will execute the query – for example, which indexes will be used, join methods, etc. This is an important tool for performance tuning and optimization.

---

**Complete the SQL code:** Fill in the missing part of this query to assign a rank number to each employee based on descending order of salary (highest salary gets rank 1).

```sql
SELECT name, salary,
       ____________ OVER (ORDER BY salary DESC) AS salary_rank
FROM Employees;
```

**Answer:**

```sql
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS salary_rank
FROM Employees;
```

**Explanation:** The window function `ROW_NUMBER()` will generate a sequential rank (1, 2, 3, …) for each row based on the order specified. Here, `ROW_NUMBER() OVER (ORDER BY salary DESC)` assigns rank 1 to the highest salary, 2 to the next, and so on. (Other window functions like `RANK()` or `DENSE_RANK()` could also be used for ranking with slightly different behavior on ties.)

---

**Correct the SQL code:** The following CTE is incorrectly written and causes a syntax error. Rewrite it correctly.

```sql
WITH RecentOrders AS
    SELECT *
    FROM Orders
    WHERE OrderDate > '2025-01-01'
SELECT * FROM RecentOrders;
```

**Answer:**

```sql
WITH RecentOrders AS (
    SELECT *
    FROM Orders
    WHERE OrderDate > '2025-01-01'
)
SELECT *
FROM RecentOrders;
```

**Explanation:** When defining a Common Table Expression, you must put the subquery in parentheses after the alias. The correct format is `WITH CTE_Name AS (<subquery>) SELECT ... FROM CTE_Name;`. In the original, the parentheses and AS placement were wrong. The corrected version properly encapsulates the subquery for `RecentOrders`.

---

**Multiple correct answers:** Which of the following practices can help improve SQL query performance? (Select all that apply.)

A. Create indexes on columns that are frequently used in WHERE clauses or JOINS.  
B. Return only the columns you need in the SELECT clause (avoid SELECT *).  
C. Use a subquery for every JOIN to simplify the query.  
D. Examine the query’s execution plan and optimize any expensive operations.  

**Answer:** A, B, and D.

**Explanation:** To optimize performance: (A) Adding indexes on commonly filtered or joined columns can speed up data retrieval significantly. (B) Selecting only required columns reduces the amount of data transferred and processed (making the query more efficient than using SELECT *). (D) Analyzing the execution plan (using tools like EXPLAIN) helps identify bottlenecks – you can then add indexes or rewrite the query based on that insight. (Option C is not recommended – in fact, unnecessarily replacing JOINs with subqueries can often hurt performance or make queries more complex. Generally, use joins where appropriate; use subqueries or CTEs for logic that can’t be achieved with a straightforward join.)

