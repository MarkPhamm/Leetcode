# Write your MySQL query statement below
with ranking as (
SELECT
    store_id, 
    rank() over(partition by store_id order by price desc) rank_desc,
    rank() over(partition by store_id order by price) rank_asc,
    product_name,
    quantity
FROM inventory
), 
grouping_store as (
select 
    store_id, 
    group_concat(case when rank_desc = 1 then product_name end) most_exp_product, 
    group_concat(case when rank_desc = 1 then quantity end) most_exp_product_quantity,
    group_concat(case when rank_asc = 1 then product_name end) cheapest_product, 
    group_concat(case when rank_asc = 1 then quantity end) cheapest_product_quantity
from ranking
group by 1
)

select 
    store_id, 
    store_name, 
    location, 
    most_exp_product, 
    cheapest_product,
    round((cheapest_product_quantity+0.0)/(most_exp_product_quantity+0.0),2) imbalance_ratio
from grouping_store
join stores using(store_id)
where store_id in (select store_id from inventory group by 1 having count(product_name) >= 3)
and round((cheapest_product_quantity+0.0)/(most_exp_product_quantity+0.0),2) > 1
order by imbalance_ratio desc, store_id