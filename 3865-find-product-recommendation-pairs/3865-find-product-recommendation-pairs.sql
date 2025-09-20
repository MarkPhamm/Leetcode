# Write your MySQL query statement below
with joining_product_info as (
    select 
        product_id, 
        category,
        user_id 
    from ProductPurchases pp
    left join ProductInfo 
    using(product_id)
)

select 
    l.product_id as product1_id, 
    r.product_id as product2_id, 
    l.category as product1_category, 
    r.category as product2_category,
    count(*) customer_count
from joining_product_info l
cross join joining_product_info r
on l.product_id < r.product_id
and l.user_id = r.user_id
group by 1,2,3,4
having count(*) >= 3
order by customer_count desc, product1_id, product2_id