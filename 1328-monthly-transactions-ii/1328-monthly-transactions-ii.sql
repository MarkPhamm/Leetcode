# Write your MySQL query statement below

with approved AS
(
SELECT
    date_format(trans_date, "%Y-%m") as month,
    country,
    COUNT(CASE WHEN state = "approved" THEN id ELSE NULL end) as approved_count,
    SUM(CASE WHEN state = "approved" THEN amount ELSE NULL end) as approved_amount
FROM Transactions
GROUP BY 1,2
),
chargebacks as
(
SELECT
    date_format(Chargebacks.trans_date, "%Y-%m") as month,
    country,
    COUNT(CASE WHEN trans_id IS NOT NULL THEN trans_id ELSE NULL end) as chargeback_count,
    SUM(CASE WHEN trans_id IS NOT NULL THEN amount ELSE NULL end) as chargeback_amount
FROM Transactions
LEFT JOIN Chargebacks
ON Transactions.id = Chargebacks.trans_id
WHERE Chargebacks.trans_date IS NOT NULL
GROUP BY 1,2
)

SELECT 
    month, 
    country, 
    IFNULL(approved_count,0) as approved_count, 
    IFNULL(approved_amount,0) as approved_amount, 
    IFNULL(chargeback_count,0) as chargeback_count, 
    IFNULL(chargeback_amount,0) as chargeback_amount
FROM approved
LEFT JOIN chargebacks
USING(month, country)
WHERE approved_count > 0 OR approved_amount > 0 OR chargeback_count > 0 OR chargeback_amount > 0
UNION
SELECT 
    month, 
    country, 
    IFNULL(approved_count,0) as approved_count, 
    IFNULL(approved_amount,0) as approved_amount, 
    IFNULL(chargeback_count,0) as chargeback_count, 
    IFNULL(chargeback_amount,0) as chargeback_amount
FROM approved
RIGHT JOIN chargebacks
USING(month, country)
WHERE approved_count > 0 OR approved_amount > 0 OR chargeback_count > 0 OR chargeback_amount > 0