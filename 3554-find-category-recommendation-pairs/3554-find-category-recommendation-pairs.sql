# Write your MySQL query statement below
with base as (
    select 
        user_id,
        product_id,
        category
    from ProductPurchases
    join ProductInfo
    using(product_id)
)

select
    case 
        when x.category < y.category then x.category 
        else y.category
    end as category1,
    case 
        when x.category > y.category then x.category 
        else y.category
    end as category2,
    count(distinct x.user_id) customer_count 
from base x
join base y
on x.user_id = y.user_id
and x.product_id < y.product_id
where case 
        when x.category < y.category then x.category 
        else y.category
    end !=
    case 
        when x.category > y.category then x.category 
        else y.category
    end
group by 1,2
having count(distinct x.user_id) >= 3
order by 3 desc, 1,2
