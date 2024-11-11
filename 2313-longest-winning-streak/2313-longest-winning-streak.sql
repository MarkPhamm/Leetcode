-- Write your MySQL query statement below
WITH previous_results AS (
    SELECT 
        *,
        LAG(result) OVER (PARTITION BY player_id ORDER BY match_day) AS prev_results
    FROM Matches
),
streak_signals AS (
    SELECT 
        *,
        CASE 
            WHEN result = 'Win' AND prev_results = 'Win' THEN 0 
            ELSE 1 
        END AS streak_signal
    FROM previous_results
),
streak_groups AS (
    SELECT 
        *, 
        SUM(streak_signal) OVER (ORDER BY player_id, match_day) AS streak_group
    FROM streak_signals
),
total_wins AS (
    SELECT 
        player_id,
        streak_group,
        SUM(CASE WHEN result = 'Win' THEN 1 ELSE 0 END) AS total_win,
        RANK() OVER (PARTITION BY player_id ORDER BY SUM(CASE WHEN result = 'Win' THEN 1 ELSE 0 END) DESC) AS ranking
    FROM streak_groups
    GROUP BY player_id, streak_group
)
SELECT DISTINCT 
    player_id, 
    total_win AS longest_streak
FROM total_wins
WHERE ranking = 1;
