# Write your MySQL query statement below

with recursive month_cte as (
    select 1 as month 
    union all
    select month + 1
    from month_cte
    where month < 12
), 

active_drivers_agg as (
        select 
            case 
                when year(join_date) < 2020 then 1
                else month(join_date)
            end as month,
            count(driver_id) as active_drivers
        from drivers 
        where year(join_date) <= 2020
        group by 1 
),

calc_cumulative_drivers as (
    select 
        month, 
        sum(coalesce(active_drivers, 0)) over(order by month) cum_active_drivers
    from month_cte 
    left join active_drivers_agg 
    using(month) 
),

rides_agg as (
    select 
        month(requested_at) month,
        count(distinct driver_id) as number_of_ride 
    from AcceptedRides
    join Rides
    using(ride_id)
    where year(requested_at) = 2020 
    group by 1
),

calc_cumulative_rides as (
    select 
        month, 
        coalesce(number_of_ride, 0) number_of_ride
    from month_cte 
    left join rides_agg 
    using(month) 
)

select 
    month, 
    ifnull(round(number_of_ride*100/cum_active_drivers,2),0) working_percentage
from calc_cumulative_rides
left join calc_cumulative_drivers 
using(month)
order by 1 