# Write your MySQL query statement below
SELECT 
(SELECT max(assignment1+assignment2+assignment3) FROM scores)
-
(SELECT min(assignment1+assignment2+assignment3) FROM scores)
difference_in_score