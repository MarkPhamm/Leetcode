# Write your MySQL query statement below

SELECT distinct id, company, salary FROM 
(
SELECT  
    *,
    ROW_NUMBER() OVER(PARTITION BY company ORDER BY salary, id) ranking,
    (COUNT(*) OVER(PARTITION BY company)+1)/2 as middle  
FROM Employee
) a
WHERE middle = ranking
OR ABS(middle-ranking) = 0.5