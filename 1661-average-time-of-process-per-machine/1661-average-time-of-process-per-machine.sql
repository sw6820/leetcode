# Write your MySQL query statement below
SELECT machine_id, ROUND((SUM(time)/COUNT(time)),3) AS processing_time
FROM (SELECT machine_id, process_id, SUM(CASE WHEN activity_type='start'THEN -timestamp ELSE timestamp END) AS time
FROM Activity
GROUP BY machine_id, process_id) AS X
GROUP BY machine_id