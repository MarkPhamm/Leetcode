# Write your MySQL query statement below

SELECT 
    tpf.team_name as team_name,
    CASE WHEN time_stamp <= '45:00' THEN 1 ELSE 2 END half_number,
    SUM(CASE WHEN tpf.team_name = tpt.team_name THEN 1 ELSE -1 END) dominance
FROM Passes
JOIN Teams tpf ON Passes.pass_from = tpf.player_id
JOIN Teams tpt ON Passes.pass_to = tpt.player_id
GROUP BY 1,2  
ORDER BY 1,2