# Write your MySQL query statement below


with base as (
    select
        distinct 
        x.user_id user_id, 
        y.user_id recommended_id,
        x.day,
        x.song_id x_song_id, 
        y.song_id y_song_id
    from Listens x
    join Listens y
    on x.song_id = y.song_id
    and x.day = y.day
    and x.user_id != y.user_id
),

friends_comb as (
    select 
        concat(user1_id ,'-', user2_id) as combination
    from Friendship
    union all 
    select 
        concat(user2_id ,'-',  user1_id) as combination
    from Friendship
),

adding_day_granularity as (
select 
    user_id,
    recommended_id,
    day
from base 
where concat(user_id ,'-',  recommended_id) not in (select combination from friends_comb)
group by 1,2,3
having count(*) >= 3
)

select 
    distinct 
    user_id,
    recommended_id
from adding_day_granularity
order by 1,2