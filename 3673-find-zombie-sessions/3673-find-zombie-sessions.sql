# Write your MySQL query statement below


select 
    session_id, 
    user_id, 
    TIMESTAMPDIFF(MINUTE, min(event_timestamp), max(event_timestamp)) AS session_duration_minutes,
    count(case when event_type = 'scroll' then event_id else null end) scroll_count
from app_events
group by 1, 2
having count(case when event_type = 'purchase' then event_id else null end) < 1
and TIMESTAMPDIFF(MINUTE, min(event_timestamp), max(event_timestamp)) >= 30
and count(case when event_type = 'click' then event_id else null end) / 
    count(case when event_type = 'scroll' then event_id else null end) < 0.2
and count(case when event_type = 'scroll' then event_id else null end) >= 5
order by scroll_count desc, session_id
