WITH recursive ids AS
(
    SELECT 1 as id 
    UNION ALL
    SELECT id+1 as id FROM ids
    WHERE id < (SELECT MAX(customer_id) FROM Customers)
)
SELECT id as ids FROM ids
LEFT JOIN customers
ON ids.id = customers.customer_id
WHERE customer_id is NULL