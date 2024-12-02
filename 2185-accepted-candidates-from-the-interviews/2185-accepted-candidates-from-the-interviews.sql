# Write your MySQL query statement below

WITH total_scores AS (
    SELECT 
        interview_id, SUM(score) score
    FROM Rounds
    GROUP BY 1    
)
SELECT candidate_id FROM Candidates
JOIN total_scores 
USING(interview_id)
WHERE years_of_exp >= 2
AND score > 15