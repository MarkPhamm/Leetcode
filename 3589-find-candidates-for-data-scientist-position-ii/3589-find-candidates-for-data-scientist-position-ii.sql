-- Write your MySQL query statement below
WITH cte1 AS (
    SELECT 
        project_id, 
        candidate_id,
        GROUP_CONCAT(skill ORDER BY skill) AS candidate_skills
    FROM Projects
    JOIN Candidates USING (skill)
    GROUP BY project_id, candidate_id
),
cte2 AS (
    SELECT 
        project_id, 
        GROUP_CONCAT(skill ORDER BY skill) AS required_skills 
    FROM Projects
    GROUP BY project_id
),
cte3 AS (
    SELECT 
        project_id, 
        candidate_id
    FROM cte1
    JOIN cte2 USING (project_id)
    WHERE candidate_skills = required_skills
    GROUP BY project_id, candidate_id
)

SELECT project_id, candidate_id, score 
FROM (
    SELECT 
        Projects.project_id, 
        candidate_id,
        100 + SUM(
            CASE 
                WHEN proficiency > importance THEN 10
                WHEN proficiency < importance THEN -5
                ELSE 0
            END
        ) AS score,
        RANK() OVER (
            PARTITION BY project_id 
            ORDER BY 
                SUM(
                    CASE 
                        WHEN proficiency > importance THEN 10
                        WHEN proficiency < importance THEN -5
                        ELSE 0
                    END
                ) DESC, 
                candidate_id
        ) AS ranking
    FROM Candidates
    JOIN Projects USING (skill)
    JOIN cte3 USING (candidate_id, project_id)
    GROUP BY project_id, candidate_id
) AS a
WHERE ranking = 1
ORDER BY project_id;
