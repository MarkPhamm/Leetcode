# Write your MySQL query statement below
select b.id from weather a,weather b 
where Datediff (b.RecordDate, a.RecordDate) =1  and a.temperature < b.temperature 