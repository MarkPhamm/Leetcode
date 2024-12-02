# Write your MySQL query statement below

SELECT
    member_id, 
    name, 
    CASE 
        WHEN (COUNT(CASE WHEN charged_amount IS NOT NULL THEN 1 ELSE NUll END)+0.0)/COUNT(visit_id) IS NULL THEN "Bronze"
        WHEN (COUNT(CASE WHEN charged_amount IS NOT NULL THEN 1 ELSE NUll END)+0.0)/COUNT(visit_id)*100 < 50 THEN "Silver" 
        WHEN (COUNT(CASE WHEN charged_amount IS NOT NULL THEN 1 ELSE NUll END)+0.0)/COUNT(visit_id)*100 < 80 THEN "Gold" 
        ELSE "Diamond"
    END AS category 
FROM Members
LEFT JOIN Visits USING(member_id)
LEFT JOIN Purchases USING(visit_id)
GROUP BY 1,2
