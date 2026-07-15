-- Week 1 Day 2: SQL Joins

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
INSERT INTO Customers VALUES (1,'Archana');
INSERT INTO Customers VALUES (2,'Ravi');
INSERT INTO Customers VALUES (3,'Priya');

-- Insert data into Orders
INSERT INTO Orders VALUES (101,1,'Laptop');
INSERT INTO Orders VALUES (102,2,'Phone');
INSERT INTO Orders VALUES (103,1,'Mouse');

-- INNER JOIN
SELECT c.customer_name, o.product
FROM Customers c
INNER JOIN Orders o
ON c.customer_id = o.customer_id;

-- LEFT JOIN
SELECT c.customer_name, o.product
FROM Customers c
LEFT JOIN Orders o
ON c.customer_id = o.customer_id;

-- RIGHT JOIN
-- SQLite does not support RIGHT JOIN directly.

-- FULL OUTER JOIN
-- SQLite does not support FULL OUTER JOIN directly.
-- Alternative using UNION

SELECT c.customer_name, o.product
FROM Customers c
LEFT JOIN Orders o
ON c.customer_id = o.customer_id

UNION

SELECT c.customer_name, o.product
FROM Orders o
LEFT JOIN Customers c
ON o.customer_id = c.customer_id;

-- Create Employees table
CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    manager_id INTEGER
);

-- Insert Employees
INSERT INTO Employees VALUES (1,'Ramesh',NULL);
INSERT INTO Employees VALUES (2,'Sita',1);
INSERT INTO Employees VALUES (3,'Rahul',1);
INSERT INTO Employees VALUES (4,'Anita',2);

-- SELF JOIN
SELECT
e1.employee_name,
e2.employee_name AS manager
FROM Employees e1
JOIN Employees e2
ON e1.manager_id = e2.employee_id;