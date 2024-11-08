# Write your MySQL query statement below

SELECT distinct title FROM Content
JOIN TVProgram
USING(content_id)
WHERE DATE_FORMAT(program_date, "%Y-%m") = "2020-06"
AND Kids_content = "Y"
AND content_type = "Movies"