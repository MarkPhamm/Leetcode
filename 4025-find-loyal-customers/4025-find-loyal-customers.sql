# Write your MySQL query statement below

select 
    customer_id
from customer_transactions 
group by 1
having count(transaction_id) >= 3
and (count(case when transaction_type = 'refund' then transaction_id else null end)+0.0)/count(transaction_id) < 0.2
and datediff(max(transaction_date), min(transaction_date)) >= 30
order by 1 