with recursive year_bounds as (
    select
        customer_id,
        min(year(order_date)) as min_year,
        max(year(order_date)) as max_year
    from orders
    group by customer_id
),

all_years as (
    select
        customer_id,
        min_year as year_order,
        max_year
    from year_bounds
    
    union all
    
    select
        customer_id,
        year_order + 1,
        max_year
    from all_years
    where year_order + 1 <= max_year
), 

calc_yearly_total as (
select 
    customer_id, 
    year(order_date) year_order, 
    sum(price) total
from Orders 
group by 1,2 
),


calc_prev_total as (
select 
    customer_id, 
    year_order, 
    coalesce(total, 0) total,
    coalesce(lag(coalesce(total, 0)) over(partition by customer_id order by year_order),0) prev_total
from all_years 
left join calc_yearly_total
using(year_order, customer_id)
)

select 
    distinct customer_id 
from Orders
where customer_id not in 
(
    select distinct customer_id from calc_prev_total
    where prev_total >= total 
)

