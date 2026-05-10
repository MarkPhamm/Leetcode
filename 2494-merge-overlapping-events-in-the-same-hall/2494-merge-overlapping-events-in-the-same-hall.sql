# Write your MySQL query statement below
-- Write a solution to merge all the overlapping events that are held in the same hall. Two events overlap if they have at least one day in common.
-- gaps and island again lol
-- similar to merge interval 

with calc_end_day_range as (
    select 
        *, 
        # max of end date of all row before the current row 
        max(end_day) over(partition by hall_id order by start_day rows between unbounded preceding and 1 preceding) as end_day_range 
    from HallEvents
), 
calc_streak_start as (
    select 
        *, 
        if(start_day > end_day_range,1,0) as streak_start
    from calc_end_day_range
), 

calc_group as (
    select 
        *, 
        sum(streak_start) over(partition by hall_id order by start_day) group_id
    from calc_streak_start
)

select 
    hall_id, 
    min(start_day) start_day, 
    max(end_day) end_day
from calc_group
group by hall_id, group_id 