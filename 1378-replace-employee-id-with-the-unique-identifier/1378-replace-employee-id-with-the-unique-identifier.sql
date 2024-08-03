# Write your MySQL query statement below
SELECT unique_id, IFNULL(name,null) AS name
FROM Employees AS E
LEFT JOIN EmployeeUNI AS U
ON E.id = U.id
