with cte as (
    select 
        id, height,
        max(height) over(order by id) as "max_height_left",
        max(height) over(order by id desc) as "max_height_right",
        
        least(
            max(height) over(order by id),
            max(height) over(order by id desc)
        ) potential_water

    from Heights
)
select 
    sum(potential_water - height) total_trapped_water
from cte 