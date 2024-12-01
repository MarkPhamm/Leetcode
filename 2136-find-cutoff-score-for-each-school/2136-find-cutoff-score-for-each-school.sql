# Write your MySQL query statement below

SELECT 
    school_id,
    IFNULL(MIN(score),-1) as score
FROM schools
LEFT JOIN exam ON schools.capacity >= student_count
GROUP BY 1