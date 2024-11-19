# Write your MySQL query statement below


SELECT 
    CASE
    WHEN (SELECT COUNT(IF(score>=90,1,NULL)) FROM NewYork) >  (SELECT COUNT(IF(score>=90,1,NULL)) FROM California) THEN "New York University"
    WHEN (SELECT COUNT(IF(score>=90,1,NULL)) FROM NewYork) <  (SELECT COUNT(IF(score>=90,1,NULL)) FROM California) THEN "California University"
    ELSE "No Winner" 
    END AS winner