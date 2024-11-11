# Write your MySQL query statement below
select s.seller_name from Seller s
where not exists (
    select 1 from Orders o
    where o.seller_id = s.seller_id and year(sale_date) = 2020
)
order by seller_name