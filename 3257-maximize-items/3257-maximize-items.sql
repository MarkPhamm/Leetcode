# Write your MySQL query statement below
with agg_inventory as(
    select
        item_type,
        COUNT(*) total_items,
        SUM(square_footage) total_square_footage
    from Inventory
    group by 1
),
prime as(
    select 
        item_type, 
        total_items,
        floor(500000/total_square_footage) * total_items prime_item_count,
        500000 - floor(500000/total_square_footage) * total_square_footage remaining
    from agg_inventory
    where item_type = 'prime_eligible'
),
not_prime as(
    select
        item_type, 
        total_items,
        total_square_footage
    from agg_inventory
    where item_type = 'not_prime'
),
remaining_calc as (
    select 
        prime.item_type as prime_item_type,
        prime.total_items as prime_total_items,
        prime.prime_item_count,
        not_prime.item_type as np_item_type,
        floor(remaining/not_prime.total_square_footage) * not_prime.total_items as np_item_count
    from prime
    join not_prime
)

select prime_item_type as item_type, prime_item_count as item_count
from remaining_calc 
union
select np_item_type as item_type, np_item_count as item_count
from remaining_calc 
order by 2 desc

