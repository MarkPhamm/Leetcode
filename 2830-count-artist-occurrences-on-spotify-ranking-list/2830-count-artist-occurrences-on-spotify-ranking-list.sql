# Write your MySQL query statement below
SELECT artist, COUNT(id) occurrences 
FROM Spotify
GROUP BY 1
ORDER BY 2 DESC,1