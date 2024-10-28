# Write your MySQL query statement below
select  score, dense_rank()over(
        ORDER BY score desc
        ) as "rank"
from Scores order by score desc;
