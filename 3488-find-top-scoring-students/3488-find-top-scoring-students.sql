# Write your MySQL query statement below
SELECT student_id FROM
(
SELECT 
student_id, 
COUNT(distinct course_id) number_of_courses, 
COUNT(IF(grade = 'A', 1, NULL)) number_of_As 
FROM students
JOIN courses using(major)
LEFT JOIN enrollments USING(course_id, student_id)
GROUP BY 1
) a
WHERE number_of_courses = number_of_As
ORDER BY 1

