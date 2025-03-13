# PostgreSQL Cheat Sheet

## Overview

### What is PostgreSQL?
**Definition:** PostgreSQL is an advanced, open-source object-relational database system.

**Key Features:**
- ACID compliance
- Extensibility
- Support for advanced data types (JSON, arrays, GIS data with PostGIS)
- Adherence to SQL standards

**Philosophy:** Designed to be reliable, robust, and scalable for both simple applications and complex, enterprise-level systems.

### Why Use PostgreSQL?
- **Reliability & Integrity:** Full ACID compliance ensures reliable transactions.
- **Extensibility:** Create custom functions, data types, and operators.
- **Scalability:** Suitable for small projects and large-scale, concurrent user environments.
- **Community & Ecosystem:** Strong community and a wide range of extensions (e.g., PostGIS for spatial data).

### When to Use PostgreSQL?
- **Enterprise Applications:** Strong data integrity and complex transactions.
- **Web Development:** Backend for web apps requiring structured data storage.
- **Data Warehousing & Analytics:** Robust querying capabilities and large datasets.
- **GIS and Spatial Applications:** Use extensions like PostGIS for geographic data.

## How to Use PostgreSQL?

### Installation & Setup
- Download from PostgreSQL’s website or use package managers (`apt`, `yum`, `brew`).

#### Database Creation:
```bash
createdb mydb
```

### Basic psql Commands
#### List Databases:
```sql
\l
```
#### Connect to a Database:
```sql
\c mydb
```
#### List Tables:
```sql
\dt
```
#### Describe a Table:
```sql
\d tablename
```

### Essential SQL Commands
#### Creating a Table:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);
```
#### Inserting Data:
```sql
INSERT INTO users (name, email)
VALUES ('Alice', 'alice@example.com');
```
#### Querying Data:
```sql
SELECT * FROM users;
```

## Intermediate Topics

### Joins and Subqueries
#### Example of an INNER JOIN:
```sql
SELECT u.name, o.order_date
FROM users u
JOIN orders o ON u.id = o.user_id;
```
#### Subquery Example:
```sql
SELECT name
FROM users
WHERE id IN (SELECT user_id FROM orders WHERE order_date > '2025-01-01');
```

### Indexing
#### Creating an Index:
```sql
CREATE INDEX idx_users_email ON users(email);
```

### Views and Materialized Views
#### Creating a View:
```sql
CREATE VIEW active_users AS
SELECT * FROM users WHERE active = true;
```
#### Creating a Materialized View:
```sql
CREATE MATERIALIZED VIEW summary AS
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id;
```

### Transactions & Locking
#### Using Transactions:
```sql
BEGIN;
  -- Execute your SQL commands
COMMIT;
```
#### Rolling Back:
```sql
ROLLBACK;
```

### Functions and Stored Procedures
#### Creating a Simple Function:
```sql
CREATE FUNCTION add_numbers(a INT, b INT) RETURNS INT AS $$
  SELECT a + b;
$$ LANGUAGE SQL;
```

## Advanced Topics

### Performance Tuning
#### Using EXPLAIN:
```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'alice@example.com';
```
#### Optimizing Queries:
Regularly analyze query plans and adjust indexes, rewrite queries, or use caching strategies.

### Partitioning
#### Table Partitioning Example:
```sql
CREATE TABLE measurement (
  logdate DATE,
  peaktemp INT,
  unitsales INT
) PARTITION BY RANGE (logdate);
```
#### Creating a Partition:
```sql
CREATE TABLE measurement_2025 PARTITION OF measurement
FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
```

### Replication and High Availability
- **Streaming Replication:** Configure master-slave replication for load balancing and redundancy.
- Look into parameters like `wal_level`, `max_wal_senders`, and `hot_standby`.

### Advanced Indexing
#### GIN and GiST Indexes:
- **GIN (Generalized Inverted Index):** Useful for full-text search and array data.
- **GiST (Generalized Search Tree):** Often used with spatial data or custom data types.

### Security and Access Control
#### Roles and Permissions:
```sql
CREATE ROLE readonly NOINHERIT;
GRANT CONNECT ON DATABASE mydb TO readonly;
GRANT USAGE ON SCHEMA public TO readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
```
#### Row-Level Security (RLS):
```sql
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
CREATE POLICY user_policy ON users
  USING (id = current_setting('myapp.current_user_id')::INT);
```

### Extensions
#### Installing Extensions (e.g., PostGIS):
```sql
CREATE EXTENSION postgis;
```

### Backup and Recovery
#### Backing Up a Database:
```bash
pg_dump mydb > mydb_backup.sql
```
#### Restoring a Database:
```bash
psql mydb < mydb_backup.sql
```

## Tips and Best Practices
- **Regular Backups:** Automate your backup process.
- **Monitoring:** Use tools like `pg_stat_activity` and `pg_stat_database` for performance insights.
- **Indexes:** Regularly review and optimize your indexing strategy.
- **Security:** Use roles, permissions, and RLS to secure sensitive data.
- **Updates:** Keep PostgreSQL updated to leverage new features and security fixes.

