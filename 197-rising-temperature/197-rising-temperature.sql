# Write your MySQL query statement below
SELECT W2.id
FROM Weather AS W1
JOIN Weather AS W2
WHERE W1.temperature < W2.temperature AND DATEDIFF(W2.recordDate,W1.recordDate)=1