# Write your MySQL query statement below
SELECT name, IFNULL(bonus,null) AS bonus
FROM Employee
LEFT JOIN Bonus
USING (empId)
WHERE bonus IS NULL OR bonus<1000