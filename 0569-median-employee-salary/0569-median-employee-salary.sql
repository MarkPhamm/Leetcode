# Write your MySQL query statement below

with cte as (
    select
        id, 
        company,
        salary,
        row_number() over (partition by company order by salary) as rnk,
        (count(*) over (partition by company)+1)/2 as middle
    from Employee
    order by company, rnk
)
select
    distinct 
    id,
    company,
    salary
    from cte 
where 
    rnk=middle or
    abs(middle-rnk)=0.5