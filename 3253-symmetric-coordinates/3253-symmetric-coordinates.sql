# Write your MySQL query statement below
WITH Coordinates_id AS
(
    SELECT ROW_NUMBER() OVER(ORDER BY X,Y) ranking, X,Y FROM Coordinates 
)

SELECT Distinct x.X, x.Y FROM Coordinates_id x
JOIN Coordinates_id y
ON x.X = y.Y and x.Y = y.X and x.X <= x.Y and x.ranking != y.ranking
ORDER BY 1,2