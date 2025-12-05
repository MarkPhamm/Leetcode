# Write your MySQL query statement below
with recursive base as (
    select
        post_id, 
        substring_index(content, ' ', 1) c,
        substring(content, length(substring_index(content, ' ', 1))+2) remaining,
        1 as pos
    from posts

    union all 

    select
        post_id, 
        substring_index(remaining, ' ', 1) c,
        substring(remaining, length(substring_index(remaining, ' ', 1))+2) remaining, 
        pos + 1 as pos 
    from base
    where length(remaining) > 0
)

select 
    post_id, 
    coalesce(group_concat(distinct topic_id order by topic_id), 'Ambiguous!')  topic
from base
left join Keywords on base.c = Keywords.word
group by 1 
order by post_id, pos