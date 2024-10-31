# Write your MySQL query statement below
SELECT AVG(num)  as median FROM
(
SELECT 
    *, 
    SUM(frequency) OVER(ORDER BY num) - (frequency-1) as starting_location,
    SUM(frequency) OVER(ORDER BY num) as ending_location,
    FLOOR((SUM(frequency) OVER()+1)/2) as lower_index,
    CEIL((SUM(frequency) OVER()+1)/2) as upper_index
FROM 
    Numbers
) a
WHERE lower_index BETWEEN starting_location AND ending_location
OR upper_index BETWEEN starting_location AND ending_location
