SELECT 
    season_id,
    team_id, 
    team_name,
    wins*3+draws as points,
    goals_for - goals_against goal_difference,
    DENSE_RANK() OVER(PARTITION BY season_id ORDER BY wins*3+draws DESC, goals_for - goals_against DESC) position
FROM SeasonStats
ORDER BY season_id, position, team_name