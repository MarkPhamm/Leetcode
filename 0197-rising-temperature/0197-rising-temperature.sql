# Write your MySQL query statement below
# Write your MySQL query statement below
select b.id from weather a 
join weather b 
on a.recordDate  + INTERVAL 1 DAY = b.recordDate
AND a.temperature < b.temperature 