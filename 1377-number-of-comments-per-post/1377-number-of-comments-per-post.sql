# Write your MySQL query statement below
select 
    filtered.post as post_id,
    count(distinct Submissions.sub_id) as number_of_comments
from 
    (select sub_id as post
    from Submissions
    where parent_id is null) filtered
left join 
    Submissions
on filtered.post = submissions.parent_id
group by post
order by post asc