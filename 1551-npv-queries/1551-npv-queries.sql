# Write your MySQL query statement below
SELECT 
    id,
    year,
    ifnull(npv,0) npv
FROM Queries
LEFT JOIN NPV USING(id,year)