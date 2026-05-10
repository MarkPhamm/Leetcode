# Write your MySQL query statement below
-- classic gaps and island
-- A user is considered behaviorally stable if there exists a sequence of at least 5 consecutive days such that:
-- The user performed exactly one action per day during that period.
-- The action is the same on all those consecutive days.
-- If a user has multiple qualifying sequences, only consider the sequence with the maximum length.
with calc_prev_date as (
    select
        *,
        lag(action_date) over(partition by user_id, action order by action_date) prev_date
    from activity 
), 

calc_streak_start as (
select 
    *, 
    case 
        when prev_date is null or datediff(action_date, prev_date) != 1 then 1
        else 0 
    end as streak_start
from calc_prev_date
),

calc_groups as (
    select 
        *, 
        sum(streak_start) over(partition by user_id order by action, action_date) group_id
    from calc_streak_start 
), 

agg_at_group_level as (
select 
    user_id, 
    action, 
    group_id, 
    count(*) streak_length,
    min(action_date) start_date, 
    max(action_date) end_date
from calc_groups
group by 1,2,3
having count(*) >= 5
),


keeping_highest_streak_per_user as (
select 
    *, 
    rank() over(partition by user_id order by streak_length desc) rnk
from agg_at_group_level
)

select 
    user_id, 
    action,
    streak_length, 
    start_date, 
    end_date 
from keeping_highest_streak_per_user
where rnk = 1
order by 3 desc, 1