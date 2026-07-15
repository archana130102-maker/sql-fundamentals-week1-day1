-- ==========================================
-- Week 1 - Day 4: SQL Subqueries & CTEs
-- ==========================================

-- Remove old Sales table
DROP TABLE IF EXISTS Sales;

-- Create Sales table
CREATE TABLE Sales (
    sale_id INTEGER PRIMARY KEY,
    region TEXT,
    salesperson TEXT,
    amount REAL
);

-- Insert sample data
INSERT INTO Sales VALUES
(1,'South','Archana',25000),
(2,'North','Ravi',18000),
(3,'South','Priya',32000),
(4,'East','Rahul',15000),
(5,'West','Anita',22000),
(6,'South','Kiran',12000),
(7,'North','Sita',28000),
(8,'East','Ramesh',17000);

-- ==========================================
-- 1. Non-Correlated Subquery
-- Find sales greater than average sales
-- ==========================================

SELECT *
FROM Sales
WHERE amount >
(
    SELECT AVG(amount)
    FROM Sales
);

-- ==========================================
-- 2. Correlated Subquery
-- Find top performer in each region
-- ==========================================

SELECT *
FROM Sales s1
WHERE amount =
(
    SELECT MAX(amount)
    FROM Sales s2
    WHERE s1.region = s2.region
);

-- ==========================================
-- 3. CTE using WITH clause
-- ==========================================

WITH AverageSales AS
(
    SELECT AVG(amount) AS AvgAmount
    FROM Sales
)

SELECT *
FROM Sales
WHERE amount >
(
    SELECT AvgAmount
    FROM AverageSales
);

-- ==========================================
-- 4. Chain Two CTEs
-- ==========================================

WITH RegionSales AS
(
    SELECT
        region,
        SUM(amount) AS TotalSales
    FROM Sales
    GROUP BY region
),

AverageRegionSales AS
(
    SELECT AVG(TotalSales) AS AvgSales
    FROM RegionSales
)

SELECT *
FROM RegionSales
WHERE TotalSales >
(
    SELECT AvgSales
    FROM AverageRegionSales
);