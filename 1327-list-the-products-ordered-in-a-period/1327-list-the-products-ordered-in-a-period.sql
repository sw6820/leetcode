# Write your MySQL query statement below
SELECT product_name, SUM(unit) AS unit
FROM Products
JOIN (
    SELECT product_id, unit
    FROM Orders
    WHERE YEAR(order_date)=2020 AND MONTH(order_date)=2    
) AS X
USING (product_id)
GROUP BY product_id
HAVING SUM(unit)>=100