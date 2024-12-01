# Write your MySQL query statement below

WITH 2021_subscriptions AS (
    SELECT * FROM subscriptions
    WHERE year(start_date) = 2021 OR year(end_date) = 2021
),
2021_streams AS (
    SELECT * FROM Streams
    WHERE year(stream_date) = 2021
)

SELECT COUNT(DISTINCT account_id) accounts_count FROM 2021_subscriptions
LEFT JOIN 2021_streams USING(account_id)
WHERE session_id IS NULL