# Write your MySQL query statement below
SELECT question_id as survey_log FROM
(
SELECT 
    question_id,
    COUNT(CASE WHEN action = 'answer' THEN 1 ELSE NULL END)/
    COUNT(CASE WHEN action = 'show' THEN 1 ELSE NULL END)
    AS rate
FROM SurveyLog
GROUP BY question_id
ORDER BY rate desc, question_Id
LIMIT 1
) a