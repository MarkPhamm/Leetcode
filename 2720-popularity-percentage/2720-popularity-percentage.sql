# Write your MySQL query statement below

with base as (
    select user1, user2 from friends
    union 
    select user2 as user1, user1 as user2 from friends 
), 

base_dedup as (
    select distinct user1, user2 from base 
)

select 
    user1, 
    round(
        count(*) * 100/ (
            select count(distinct user1) percentage_popularity from base 
        )
    ,2) percentage_popularity
from base_dedup 
group by 1 
order by 1,2