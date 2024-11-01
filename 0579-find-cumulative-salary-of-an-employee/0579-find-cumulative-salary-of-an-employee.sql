# Write your MySQL query statement below
-- SELECT *, 
-- SUM(salary) OVER(rows between 2 preceding and current row) as cumulative
-- FROM Employee
-- ORDER BY id, month


SELECT 
    id,
    month,
    salary + 
    case when previous_month = month - 1 THEN previous_salary else 0 end + 
    case when previous_previous_month = month -2 THEN previous_previous_salary else 0 end
    as Salary
FROM
(
SELECT *,
    lag(month) over(partition by id order by month) as previous_month,
    lag(salary) over(partition by id order by month) as previous_salary,
    lag(month,2) over(partition by id order by month) as previous_previous_month,
    lag(salary,2) over(partition by id order by month) as previous_previous_salary,
    rank() over(partition by id order by month desc) ranking
FROM Employee
) a
WHERE ranking != 1