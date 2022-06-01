# Write your MySQL query statement below
SELECT name
FROM SalesPerson AS S
WHERE sales_id NOT IN (
    SELECT O.sales_id
    FROM Company AS C
    RIGHT JOIN Orders AS O
    ON C.com_id = O.com_id
    WHERE name = 'RED'
)
###