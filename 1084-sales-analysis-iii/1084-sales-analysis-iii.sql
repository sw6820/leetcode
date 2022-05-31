# Write your MySQL query statement below
SELECT P.product_id, product_name
FROM Sales AS S
INNER JOIN Product AS P
ON P.product_id = S.product_id
GROUP BY product_id
HAVING 1<=MIN(MONTH(sale_date)) AND MAX(MONTH(sale_date))<=3
###