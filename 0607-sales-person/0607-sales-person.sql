# Write your MySQL query statement below
SELECT salesperson.name
FROM salesperson
WHERE salesperson.sales_id NOT IN
(
select salesperson.sales_id from Orders
left join Company
on Orders.com_id = Company.com_id
right join SalesPerson
on  Orders.sales_id = SalesPerson.sales_id
where Company.name = "RED" 
)