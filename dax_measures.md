# DAX Measures

## 1. Total Sales
```DAX
Total Sales = SUM(sales[price])
```

Calculates the total sales amount.

## 2. Total Quantity
```DAX
Total Quantity = SUM(sales[quantity])
```

Calculates the total quantity sold.

## 3. Total Orders
```DAX
Total Orders = COUNT(sales[order_id])
```

Counts the total number of orders.

## 4. Profit Margin %
```DAX
Profit Margin % = 20
```

Example calculated column for profit margin.

## 5. CALCULATE Example
```DAX
High Sales = CALCULATE(SUM(sales[price]), sales[price] > 1000)
```

Returns the total sales where the price is greater than 1000.