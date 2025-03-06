# Write your MySQL query statement below
SELECT 
    CASE WHEN id&1 AND id NOT IN (SELECT MAX(id) FROM Seat) THEN id+1
    WHEN NOT id&1 THEN id-1
    ELSE id END AS id, student
FROM Seat
ORDER BY id