# Write your MySQL query statement below

Select customer_number from Orders o
group by Customer_number
order by count(customer_number) desc limit 1;