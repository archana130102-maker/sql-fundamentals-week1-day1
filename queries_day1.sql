
SELECT * FROM sales;

SELECT customer_name FROM sales;

SELECT * FROM sales
WHERE city='Bangalore';

SELECT * FROM sales
WHERE price > 5000;

SELECT * FROM sales
WHERE city='Bangalore'
AND status='Delivered';

SELECT * FROM sales
WHERE city='Bangalore'
OR city='Mysore';

SELECT * FROM sales
WHERE NOT status='Pending';

SELECT * FROM sales
WHERE customer_name LIKE 'R%';

SELECT * FROM sales
WHERE city IN ('Bangalore','Chennai');

SELECT * FROM sales
WHERE price BETWEEN 1000 AND 60000;

SELECT * FROM sales
WHERE quantity IS NULL;