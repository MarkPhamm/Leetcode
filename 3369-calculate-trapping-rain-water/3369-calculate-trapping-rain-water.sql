with creating_max_height as (
  -- creating max_left_height and max_right_height
  select id, height,
      max(height) over(order by id) as "max_height_left",
      max(height) over(order by id desc) as "max_height_right"
  from Heights
),

creating_trapped_water_height as (
    -- trapped water will be the smaller bound between the "max_height_left" and "max_height_right"
    select 
        *,
        least(max_height_left,max_height_right) as "trapped_water_height"
    from creating_max_height
)

-- each block is basically 1 unit, so we just use sum("trapped_water_height" - height) for sum unit trapped
select sum(trapped_water_height - height) as "total_trapped_water"
from creating_trapped_water_height