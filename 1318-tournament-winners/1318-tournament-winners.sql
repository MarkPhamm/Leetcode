# Write your MySQL query statement below
with player_and_score AS
(
SELECT player_id, SUM(score) as total_score 
FROM 
(
    SELECT
        first_player as player_id,
        first_score as score
    FROM Matches
    UNION ALL
    SELECT
        second_player as player_id,
        second_score as score
    FROM Matches
    ORDER BY 1
) a
GROUP BY 1
)

SELECT group_id, player_id FROM 
(
SELECT 
*,
ROW_NUMBER() OVER(partition by group_id ORDER BY total_score DESC, player_id) ranking
FROM Players
LEFT JOIN player_and_score
USING(player_id)
) a
WHERE ranking = 1