# Write your MySQL query statement below

SELECT distinct viewer_id as id FROM
(
SELECT
viewer_id, 
view_date,
COUNT(DISTINCT article_id) AS total_view
FROM Views
GROUP BY 1,2
HAVING COUNT(DISTINCT article_id) >=2
) a
ORDER BY 1