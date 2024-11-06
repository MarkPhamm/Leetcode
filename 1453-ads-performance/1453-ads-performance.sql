# Write your MySQL query statement below

SELECT 
    ad_id,
    IFNULL(ROUND(SUM(IF(action = 'Clicked',1,0))
    /SUM(IF(action != 'Ignored',1,0))*100,2),0) ctr
FROM Ads
GROUP BY 1
ORDER BY 2 DESC, 1