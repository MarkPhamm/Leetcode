# Write your MySQL query statement below
WITH contacts_classifier AS
(
SELECT 
    user_id,
    COUNT(*) contacts_cnt, 
    COUNT(CASE WHEN contact_email in (SELECT email FROM Customers) THEN 1 ELSE NULL END) AS trusted_contacts_cnt
FROM Contacts
GROUP BY 1
)

SELECT 
    invoice_id,
    customer_name,
    price,
    IFNULL(contacts_cnt ,0) contacts_cnt,
    IFNULL(trusted_contacts_cnt ,0) trusted_contacts_cnt
FROM Invoices
JOIN Customers ON Invoices.user_id = Customers.customer_id 
LEFT JOIN contacts_classifier using(user_id)
ORDER BY 1