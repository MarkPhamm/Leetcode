# Write your MySQL query statement below
# ALL the following criteria:
-- 1. Currently have an active subscription (their last event is not cancel). check
-- 2. Have performed at least one downgrade in their subscription history.
-- 3. Their current plan revenue is less than 50% of their historical maximum plan revenue.
-- 4. Have been a subscriber for at least 60 days.
-- Return the result table ordered by days_as_subscriber in descending order, then by user_id in ascending order.

with calc_metrics as (
    select 
        *,
        rank() over(partition by user_id order by event_date desc) rnk_event,
        max(monthly_amount) over(partition by user_id) as max_historical_amount,
        max(event_date) over(partition by user_id) end_date,
        min(event_date) over(partition by user_id) start_date
    from subscription_events
)
select 
    user_id, 
    plan_name as current_plan, 
    monthly_amount as current_monthly_amount, 
    max_historical_amount,
    datediff(end_date, start_date) days_as_subscriber
from calc_metrics
where datediff(end_date, start_date) >= 60
and (monthly_amount/max_historical_amount < 0.5 and rnk_event = 1)
and user_id not in (
        select user_id 
        from calc_metrics
        where rnk_event = 1 and event_type = 'cancel'
    )
order by days_as_subscriber desc, user_id
