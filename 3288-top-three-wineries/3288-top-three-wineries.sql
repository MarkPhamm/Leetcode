# Write your MySQL query statement below
WITH stg_wineries AS (
    SELECT 
        country, 
        winery,
        SUM(points) points
    FROM Wineries
    GROUP BY 1,2
),
int_wineries AS (
    SELECT 
    
        country, 
        CONCAT(winery, ' (', points, ')') winery, 
        RANK() OVER(PARTITION BY country ORDER BY points DESC, winery) ranking
    
    FROM stg_wineries
)

SELECT 
    country, 
    GROUP_CONCAT(CASE WHEN ranking = 1 THEN winery END) AS top_winery,
    IFNULL(GROUP_CONCAT(CASE WHEN ranking = 2 THEN winery ELSE Null END),'No second winery') AS second_winery,
    IFNULL(GROUP_CONCAT(CASE WHEN ranking = 3 THEN winery ELSE Null END),'No third winery')  AS third_winery
FROM int_wineries
GROUP BY 1
ORDER BY 1
