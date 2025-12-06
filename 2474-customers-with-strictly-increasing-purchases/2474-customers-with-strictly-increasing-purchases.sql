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

yearly_totals as (
    select
        customer_id,
        year(order_date) as year_order,
        sum(price) as total
    from orders
    group by customer_id, year(order_date)
),

filled as (
    select
        a.customer_id,
        a.year_order,
        coalesce(t.total, 0) as total
    from all_years a
    left join yearly_totals t
        on a.customer_id = t.customer_id
        and a.year_order = t.year_order
),

calc_prev as (
    select
        customer_id,
        year_order,
        total,
        lag(total, 1, 0) over(partition by customer_id order by year_order) as prev_total
    from filled
)

select distinct customer_id
from calc_prev
group by customer_id
having sum(prev_total >= total) = 0;