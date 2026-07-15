-- ==========================================
-- Week 1 - Day 3: SQL Aggregations
-- GROUP BY, HAVING & Window Function
-- ==========================================

-- Remove the old Sales table if it exists
DROP TABLE IF EXISTS Sales;

-- Create Sales table
CREATE TABLE Sales (
    sale_id INTEGER PRIMARY KEY,
    region TEXT,
    category TEXT,
    month TEXT,
    amount REAL
);

-- Insert sample data
INSERT INTO Sales VALUES
(1,'South','Electronics','January',25000),
(2,'North','Furniture','January',18000),
(3,'South','Electronics','February',32000),
(4,'East','Clothing','January',15000),
(5,'West','Furniture','February',22000),
(6,'South','Clothing','March',12000),
(7,'North','Electronics','March',28000),
(8,'East','Furniture','February',17000);

-- ==========================================
-- 1. COUNT
-- ==========================================
SELECT COUNT(*) AS TotalSales
FROM Sales;

-- ==========================================
-- 2. SUM
-- ==========================================
SELECT SUM(amount) AS TotalRevenue
FROM Sales;

-- ==========================================
-- 3. AVG
-- ==========================================
SELECT AVG(amount) AS AverageSales
FROM Sales;

-- ==========================================
-- 4. MAX
-- ==========================================
SELECT MAX(amount) AS HighestSale
FROM Sales;

-- ==========================================
-- 5. MIN
-- ==========================================
SELECT MIN(amount) AS LowestSale
FROM Sales;

-- ==========================================
-- 6. GROUP BY Region
-- ==========================================
SELECT
    region,
    SUM(amount) AS TotalSales
FROM Sales
GROUP BY region;

-- ==========================================
-- 7. GROUP BY Category
-- ==========================================
SELECT
    category,
    AVG(amount) AS AverageSales
FROM Sales
GROUP BY category;

-- ==========================================
-- 8. GROUP BY Month
-- ==========================================
SELECT
    month,
    COUNT(*) AS NumberOfSales
FROM Sales
GROUP BY month;

-- ==========================================
-- HAVING
-- ==========================================
SELECT
    region,
    SUM(amount) AS TotalSales
FROM Sales
GROUP BY region
HAVING SUM(amount) > 30000;

-- ==========================================
-- Window Function (SUM OVER)
-- ==========================================
SELECT
    sale_id,
    region,
    amount,
    SUM(amount) OVER (PARTITION BY region) AS RegionTotal
FROM Sales;

-- ==========================================
-- End of Week 1 - Day 3
-- ==========================================