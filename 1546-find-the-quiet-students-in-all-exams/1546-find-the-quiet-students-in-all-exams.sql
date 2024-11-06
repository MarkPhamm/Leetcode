# Write your MySQL query statement below

WITH cte AS
(
SELECT 
    *,
    RANK() OVER(partition by exam_id ORDER BY score desc) ranking_desc,
    RANK() OVER(partition by exam_id ORDER BY score) ranking   
FROM Exam
)

SELECT * FROM student WHERE student_id IN
(
SELECT DISTINCT student_id FROM Exam
WHERE student_id not in (SELECT student_id FROM cte WHERE ranking_desc = 1 OR ranking = 1)
)