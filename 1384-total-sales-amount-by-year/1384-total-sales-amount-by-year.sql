# Write your MySQL query statement below
# Generate a date range to explode the data at a daily granularity
with recursive date_range as (
    select min(period_start) as date 
    from sales
    union all
    select DATE_ADD(date, INTERVAL 1 DAY)
    from date_range
    where date < (select max(period_end) from  sales)
)

select 
    product_id,
    product_name,
    CONVERT(year(date), char) report_year,
    sum(average_daily_sales) total_amount
from sales 
join date_range
on date_range.date between period_start and period_end
join product using(product_id)
group by 1,2,3
order by product_id, report_year