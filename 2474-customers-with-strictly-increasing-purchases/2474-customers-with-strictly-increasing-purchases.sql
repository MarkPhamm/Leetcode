# Write your MySQL query statement below
with recursive all_years as (
    select
        customer_id,
        min(year(order_date)) year_order 
    from 
        orders 
    group by 1 
    
    union all 
    
    select 
        customer_id,
        year_order + 1 year_order
    from all_years 
    where year_order < (select max(year(order_date)) from Orders)
),

calc_yearly_total as (
select 
    customer_id, 
    year(order_date) year_order, 
    sum(price) total
from Orders 
group by 1,2 
),

calc_min_max_year as (
select 
    *,
    min(year_order) over(partition by customer_id) min_year, 
    max(year_order) over(partition by customer_id) max_year
from calc_yearly_total
),

fill_null as (
select 
    *, 
    max(max_year) over(partition by customer_id) max_year_no_null,
    min(min_year) over(partition by customer_id) min_year_no_null
from all_years  
left join calc_min_max_year 
using(year_order,customer_id)
order by 2,1
), 

calc_prev_total as (
select 
    customer_id, 
    year_order, 
    coalesce(total, 0) total,
    coalesce(lag(coalesce(total, 0)) over(partition by customer_id order by year_order),0) prev_total
from fill_null
where year_order between min_year_no_null and max_year_no_null  
order by 1,2
)

select 
    distinct customer_id 
from Orders
where customer_id not in 
(
    select distinct customer_id from calc_prev_total
    where prev_total >= total 
)

-- select * from calc_prev_total
-- order by 1,2
