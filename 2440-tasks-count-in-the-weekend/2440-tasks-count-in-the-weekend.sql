# Write your MySQL query statement below
SELECT 
    COUNT(IF(WEEKDAY(submit_date) in (5,6), 1, NULL)) weekend_cnt,
    COUNT(IF(WEEKDAY(submit_date) in (0,1,2,3,4), 1, NULL)) working_cnt
FROM Tasks 
