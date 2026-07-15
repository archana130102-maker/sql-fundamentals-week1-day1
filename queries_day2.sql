-- ==========================================
-- Week 1 - Day 2: SQL Joins
-- ==========================================

-- Create Customers table
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT
);

-- Create Orders table
CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product TEXT
);

-- Insert data into Customers
INSERT INTO Customers (customer_id, customer_name) VALUES
(1, 'Archana'),
(2, 'Ravi'),
(3, 'Priya');

-- Insert data into Orders
INSERT INTO Orders (order_id, customer_id, product) VALUES
(101, 1, 'Laptop'),
(102, 2, 'Phone'),
(103, 1, 'Mouse');

-- ==========================================
-- 1. INNER JOIN
-- Returns only matching records
-- ==========================================

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.product
FROM Customers c
INNER JOIN Orders o
ON c.customer_id = o.customer_id;

-- ==========================================
-- 2. LEFT JOIN
-- Returns all customers even if they have no orders
-- ==========================================

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.product
FROM Customers c
LEFT JOIN Orders o
ON c.customer_id = o.customer_id;

-- ==========================================
-- 3. RIGHT JOIN
-- SQLite does NOT support RIGHT JOIN directly.
-- Equivalent query using LEFT JOIN by swapping tables.
-- ==========================================

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.product
FROM Orders o
LEFT JOIN Customers c
ON o.customer_id = c.customer_id;

-- ==========================================
-- 4. FULL OUTER JOIN
-- SQLite alternative using UNION
-- ==========================================

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.product
FROM Customers c
LEFT JOIN Orders o
ON c.customer_id = o.customer_id

UNION

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.product
FROM Orders o
LEFT JOIN Customers c
ON o.customer_id = c.customer_id;

-- ==========================================
-- Create Employees table for SELF JOIN
-- ==========================================

CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    manager_id INTEGER
);

-- Insert employee data

INSERT INTO Employees (employee_id, employee_name, manager_id) VALUES
(1, 'Ramesh', NULL),
(2, 'Sita', 1),
(3, 'Rahul', 1),
(4, 'Anita', 2);

-- ==========================================
-- 5. SELF JOIN
-- Display employee with manager
-- ==========================================

SELECT
    e1.employee_name AS Employee,
    e2.employee_name AS Manager
FROM Employees e1
JOIN Employees e2
ON e1.manager_id = e2.employee_id;

-- ==========================================
-- Duplicate Rows Example
-- One customer (Archana) has two orders,
-- so INNER JOIN and LEFT JOIN return two rows.
-- This is expected in a one-to-many relationship.
-- ==========================================

SELECT
    c.customer_name,
    o.product
FROM Customers c
INNER JOIN Orders o
ON c.customer_id = o.customer_id;