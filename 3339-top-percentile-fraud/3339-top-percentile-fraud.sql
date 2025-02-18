# Write your MySQL query statement below
WITH CTE AS
(
SELECT 
    *,
    PERCENT_RANK() OVER(PARTITION BY state ORDER BY fraud_score DESC) percentile
FROM Fraud
ORDER BY 2,4
)
SELECT policy_id, state, fraud_score FROM CTE
WHERE percentile < 0.05
ORDER BY 2,3,1