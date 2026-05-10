# Write your MySQL query statement below
-- Write a solution to merge all the overlapping events that are held in the same hall. Two events overlap if they have at least one day in common.
-- gaps and island again lol
-- similar to merge interval 

with calc_prev_end_day as (
select  
    *,
    lag(end_day) over(partition by hall_id order by start_day) prev_end_day
    from HallEvents
    order by end_day 
), 
calc_prev_end_day_range as (
    select  
        *, 
        max(prev_end_day) over(partition by hall_id order by start_day) prev_end_day_range
    from calc_prev_end_day
), 
calc_streaK_start as (
    select 
        *, 
        case
            when prev_end_day_range is null 
                or prev_end_day_range < start_day
            then 1
            else 0 
        end as streak_start 
    from calc_prev_end_day_range
),

calc_group as (
    select
        *, 
        sum(streak_start) over(partition by hall_id order by start_day) group_id 
    from calc_streaK_start

),

agg_group_id as (
select 
    hall_id, 
    group_id, 
    min(start_day) start_day, 
    max(end_day) end_day
from calc_group 
group by 1,2 
)

select 
    hall_id, 
    start_day, 
    end_day
from agg_group_id 