-- first cte to calculate org_level

-- | employee_id | employee_name | level |
-- | ----------- | ------------- | ----- |
-- | 1           | Alice         | 1     |
-- | 2           | Bob           | 2     |
-- | 3           | Charlie       | 2     |
-- | 4           | David         | 3     |
with recursive org_level as (
    -- base case with the executive
    select 
        employee_id, 
        employee_name,
        1 as level
    from Employees
    where manager_id is null

    union all 

    -- recursion step using the direct report to one above 
    select 
        employees.employee_id,
        employees.employee_name,
        level + 1 as level
    from employees 
    join org_level
    on employees.manager_id = org_level.employee_id
),

-- second recursive cte to see the organization rela
-- find ALL subordinate report to a manger regardless level

-- | manager_id | subordinate_id | salary |
-- | ---------- | -------------- | ------ |
-- | 1          | 1              | 12000  |
-- | 1          | 2              | 10000  |
-- | 1          | 3              | 10000  |
-- | 1          | 4              | 7500   |
-- | 1          | 5              | 7500   |
-- | 1          | 6              | 9000   |
-- | 1          | 7              | 8500   |
-- | 1          | 8              | 6000   |
-- | 1          | 9              | 7000   |
-- | 1          | 10             | 7000   |
org_rela as (
    -- base case with all current employee
    select 
        employee_id manager_id, 
        employee_id sub_id, 
        salary
    from Employees

    union all 

    select 
        org_rela.manager_id,
        employees.employee_id sub_id,
        employees.salary
    from employees
    join org_rela
    on org_rela.sub_id = employees.manager_id

)

select 
    org_level.employee_id, 
    org_level.employee_name,
    org_level.level,
    -- org rela count itself as sub
    count(org_rela.sub_id) - 1 team_size,
    sum(salary) budget
from org_level
join org_rela 
on org_level.employee_id = org_rela.manager_id
group by 1,2,3
order by 3, 5 desc, 2

