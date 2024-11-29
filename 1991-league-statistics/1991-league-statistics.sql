-- Write your MySQL query statement below
WITH points AS (
    SELECT 
        *,
        CASE 
            WHEN home_team_goals > away_team_goals THEN 3
            WHEN home_team_goals < away_team_goals THEN 0
            ELSE 1
        END AS home_team_points,
        CASE 
            WHEN home_team_goals < away_team_goals THEN 3
            WHEN home_team_goals > away_team_goals THEN 0
            ELSE 1
        END AS away_team_points
    FROM matches
),
unpivot AS (
    SELECT 
        home_team_id AS team_id, 
        home_team_points AS points, 
        home_team_goals AS goal_for, 
        away_team_goals AS goal_against
    FROM points
    UNION ALL
    SELECT 
        away_team_id AS team_id, 
        away_team_points AS points, 
        away_team_goals AS goal_for, 
        home_team_goals AS goal_against
    FROM points
)
SELECT 
    team_name,
    COUNT(*) AS matches_played,
    SUM(points) AS points,
    SUM(goal_for) AS goal_for,
    SUM(goal_against) AS goal_against,
    SUM(goal_for - goal_against) AS goal_diff
FROM unpivot
JOIN Teams USING (team_id)
GROUP BY team_name
ORDER BY points DESC, goal_diff DESC, team_name;
