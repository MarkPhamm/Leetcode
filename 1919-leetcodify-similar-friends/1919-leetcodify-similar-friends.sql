# Write your MySQL query statement below
with base as (
    select 
        l.user_id user1_id, 
        r.user_id user2_id, 
        l.day
        -- l.user_id l_id, 
        -- r.user_id r_id,
        -- l.day l_day, 
        -- r.day r_day, 
        -- l.song_id l_song_id, 
        -- r.song_id r_song_id
    from Listens l
    join Listens r 
    on l.song_id = r.song_id 
    and l.day = r.day 
    and l.user_id < r.user_id 
    group by 1,2,3
    having count(distinct l.song_id) >= 3
)
select
    distinct 
    user1_id,
    user2_id
from base
where concat(user1_id, '-', user2_id) in 
(
    select concat(user1_id, '-', user2_id) 
    from Friendship
)
order by 1,2