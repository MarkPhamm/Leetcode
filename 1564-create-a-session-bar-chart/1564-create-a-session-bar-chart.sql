# Write your MySQL query statement below
WITH CTE as
(
SELECT
    *,
    CASE 
        WHEN duration/60 > 0 AND duration/60 < 5 THEN "[0-5>"
        WHEN duration/60 >= 5 AND duration/60 < 10 THEN "[5-10>"
        WHEN duration/60 >= 10 AND duration/60 < 15 THEN "[10-15>"
        ELSE "15 or more"
    END AS bin
FROM Sessions
), 
count_of_bins AS
(
    SELECT bin, COUNT(*) AS total FROM CTE
    GROUP BY 1
),
bins_cte AS
(
    SELECT "[0-5>" bin
    UNION 
    SELECT "[5-10>" bin
    UNION
    SELECT "[10-15>" bin
    UNION
    SELECT "15 or more" bin
)


SELECT bin, IFNULL(total,0) total FROM bins_cte
LEFT JOIN count_of_bins
USING(bin)
