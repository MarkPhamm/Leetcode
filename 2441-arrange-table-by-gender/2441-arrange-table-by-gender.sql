SELECT user_id, gender FROM 
(
SELECT 
    *,
    row_number() OVER(PARTITION BY Gender ORDER BY user_id) ranking
FROM Genders
) a
ORDER BY ranking, gender