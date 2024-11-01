# Write your MySQL query statement below
-- WITH cte AS
-- (
-- SELECT project_id, RANK() OVER(ORDER BY COUNT(distinct employee_id) DESC) ranking FROM Project
-- GROUP BY 1
-- )
-- SELECT project_id FROM cte 
-- WHERE ranking = 1

# O(n Log(n))

WITH project_summary AS (
    SELECT project_id, COUNT(employee_id) AS employee_cnt
    FROM Project
    GROUP BY 1
    ORDER BY 2 DESC
)

SELECT project_id
FROM project_summary
WHERE employee_cnt = (SELECT employee_cnt FROM project_summary LIMIT 1)