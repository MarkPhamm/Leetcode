# Write your MySQL query statement below

SELECT 
    year(transaction_date) year,
    product_id,

    SUM(spend) curr_year_spend,
    LAG(SUM(spend)) OVER(PARTITION BY product_id ORDER BY year(transaction_date)) prev_year_spend,
    
    ROUND((
        SUM(spend) - 
        LAG(SUM(spend)) OVER(PARTITION BY product_id ORDER BY year(transaction_date)) 
    )/ LAG(SUM(spend)) OVER(PARTITION BY product_id ORDER BY year(transaction_date)) * 100,2) yoy_rate

FROM user_transactions
GROUP BY 2,1
ORDER BY 2,1