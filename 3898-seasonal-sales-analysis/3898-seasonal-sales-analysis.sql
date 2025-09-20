# Write your MySQL query statement below
with calculating_seasonal_stats as (
    select 
        case 
            when month(sale_date) in (12,1,2) then 'Winter'
            when month(sale_date) in (3,4,5) then 'Spring'
            when month(sale_date) in (6,7,8) then 'Summer'
            when month(sale_date) in (9,10,11) then 'Fall'
        end as season,
        category, 
        sum(quantity) total_quantity,
        sum(quantity*price) total_revenue
    from sales
    left join products 
    using (product_id)
    group by 1,2
),
calculating_ranking as (
    select 
        *,
        rank() 
            over(
                partition by season 
                order by 
                    total_quantity desc, 
                    total_revenue desc
                ) ranking 
    from calculating_seasonal_stats
    order by 1, 3 desc 
)

select 
    season, 
    category, 
    total_quantity, 
    total_revenue
from calculating_ranking 
where ranking = 1
order by season 