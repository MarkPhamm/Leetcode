# Write your MySQL query statement below
with weekly_hour_agg as (
    select  
        employee_id,
        WEEK(meeting_date, 1) week_num,
        sum(duration_hours) total_meeting_hours
    from meetings
    group by 1,2
    having sum(duration_hours) >= 20
    order by 1,2
)

select 
    employee_id, 
    employee_name,
    department, 
    count(*) as meeting_heavy_weeks
from weekly_hour_agg
join employees using(employee_id)
group by 1,2,3
having count(*) >= 2
order by 4 desc, 2