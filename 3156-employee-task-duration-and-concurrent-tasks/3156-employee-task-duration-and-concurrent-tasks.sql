with calc_max_range as (
    select 
        *, 
        max(end_time) over(
            partition by employee_id 
            order by start_time
            rows between unbounded preceding and 1 preceding
        ) as max_range
    from Tasks
), 

calc_streak_sig as (
    select
        *, 
        if(start_time < max_range, 0, 1) as streak_sig
    from calc_max_range
), 

calc_group_id as (
    select 
        *, 
        sum(streak_sig) over(
            partition by employee_id 
            order by start_time
        ) as group_id
    from calc_streak_sig
), 

agg_group_id as (
    select  
        employee_id, 
        min(start_time) as start_time, 
        max(end_time) as end_time
    from calc_group_id
    group by employee_id, group_id
),

total_hours as (
    select 
        employee_id, 
        floor(sum(timestampdiff(minute, start_time, end_time))/60) total_task_hours
    from agg_group_id
    group by employee_id
),

events as (
    select employee_id, start_time as ts, 1 as delta
    from Tasks
    
    union all
    
    select employee_id, end_time as ts, -1 as delta
    from Tasks
),

running_tasks as (
    select
        employee_id,
        ts,
        sum(delta) over(
            partition by employee_id
            order by ts, delta
        ) as active_tasks
    from events
),

max_concurrent as (
    select
        employee_id,
        max(active_tasks) as max_concurrent_tasks
    from running_tasks
    group by employee_id
)

select
    t.employee_id,
    t.total_task_hours,
    m.max_concurrent_tasks
from total_hours t
join max_concurrent m
    on t.employee_id = m.employee_id
order by 1;