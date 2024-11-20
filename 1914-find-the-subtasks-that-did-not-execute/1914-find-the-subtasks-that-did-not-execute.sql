# Write your MySQL query statement below
WITH recursive subtasks AS
(
    SELECT 1 as subtask_id
    UNION ALL
    SELECT subtask_id + 1 FROM subtasks
    WHERE subtask_id < (SELECT MAX(subtasks_count) FROM Tasks)
)
SELECT tasks.task_id, subtasks.subtask_id FROM Tasks
JOIN subtasks
ON subtasks.subtask_id <= Tasks.subtasks_count
LEFT JOIN Executed
ON executed.task_id = tasks.task_id AND executed.subtask_id = subtasks.subtask_id
WHERE executed.task_id IS NULL
ORDER BY 1,2

