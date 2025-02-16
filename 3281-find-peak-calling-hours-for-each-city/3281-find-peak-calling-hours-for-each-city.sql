# Write your MySQL query statement below
WITH call_ranking AS
(
    SELECT
        city,
        HOUR(call_time) peak_calling_hour,
        COUNT(*) number_of_calls, 
        RANK() OVER(PARTITION BY city ORDER BY COUNT(*) DESC) ranking
    FROM Calls
    GROUP BY city, HOUR(call_time)
)

SELECT city, peak_calling_hour, number_of_calls
FROM call_ranking
WHERE ranking = 1
ORDER BY 2 DESC,1 DESC