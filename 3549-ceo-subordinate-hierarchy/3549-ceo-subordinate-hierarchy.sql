# Write your MySQL query statement below
with recursive hierachy_cte as (
    select 
        employee_id, 
        employee_name, 
        0 as hierarchy_level, 
        salary
    from employees
    where manager_id is null 

    union all 
    
    select 
        e.employee_id, 
        e.employee_name, 
        hierarchy_level + 1, 
        e.salary - (SELECT salary FROM Employees WHERE manager_id IS NULL)
    from employees e
    join hierachy_cte t
    on t.employee_id = e.manager_id 
)

SELECT 
    employee_id AS subordinate_id, 
    employee_name AS subordinate_name, 
    hierarchy_level, 
    salary AS salary_difference
FROM hierachy_cte
WHERE hierarchy_level > 0
ORDER BY 3, 1