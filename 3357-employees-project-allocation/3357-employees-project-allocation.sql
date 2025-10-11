# Write your MySQL query statement below

with cacl_team_avg as (
    select 
        *,
        avg(workload) over(partition by team) team_avg
    from project 
    join employees using(employee_id)
    order by team, project_id
)

select 
    employee_id, 
    project_id, 
    name employee_name,
    workload project_workload
from cacl_team_avg
where workload > team_avg
order by 1,2