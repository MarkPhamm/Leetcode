# Write your MySQL query statement below

SELECT 
    SUBSTRING_INDEX(email, '@',-1) email_domain,
    COUNT(id) count
FROM Emails
WHERE SUBSTRING_INDEX(email, '.',-1) = 'com'
GROUP BY 1
ORDER BY 1