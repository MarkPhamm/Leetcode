-- Made at least 3 orders.
-- At least 60% of their orders are during peak hours (11:00-14:00 or 18:00-21:00).
-- Their average rating for rated orders is at least 4.0, round it to 2 decimal places.
-- Have rated at least 50% of their orders.

select
    customer_id, 
    count(distinct order_id) total_orders,
    round((count(distinct case when hour(order_timestamp) between 11 and 13 or hour(order_timestamp) between 18 and 20 then order_id else null end)+0.0)/count(distinct order_id),2)*100 peak_hour_percentage,
    round(avg(order_rating),2) average_rating
from restaurant_orders
group by 1
having count(distinct order_id) >= 3
and round((count(distinct case when hour(order_timestamp) between 11 and 13 or hour(order_timestamp) between 18 and 20 then order_id else null end)+0.0)/count(distinct order_id),2)*100 >= 60
and round(avg(order_rating),2) >= 4
and round((count(distinct case when order_rating is not null then order_id else null end)+0.0)/count(distinct order_id),2)*100 >= 50
order by average_rating desc, customer_id desc