# Write your MySQL query statement below
SELECT 
    student_id,
    course_id,
    grade
FROM
(
SELECT 
    student_id,
    course_id,
    grade,
    RANK() OVER(PARTITION BY student_id ORDER BY grade DESC, course_id) ranking
FROM Enrollments
) a
WHERE ranking = 1