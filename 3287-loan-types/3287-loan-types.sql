# Write your MySQL query statement below

SELECT 
    user_id
FROM Loans
WHERE loan_type IN ("Refinance", "Mortgage")
GROUP BY 1
HAVING COUNT(DISTINCT loan_type) = 2