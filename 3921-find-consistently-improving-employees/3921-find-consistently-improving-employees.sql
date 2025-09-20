# Write your MySQL query statement below
with calculating_ranking as (
    select 
        employee_id, 
        review_id, 
        review_date, 
        name, 
        rating,
        rank() over(
            partition by employee_id 
            order by review_date desc
        ) ranking
    from performance_reviews 
    left join employees 
    using (employee_id)
),
calculating_stats as (
    select 
        employee_id, 
        name, 
        rating,
        review_date,
        lead(rating) over(
            partition by employee_id 
            order by review_date desc
        ) prev_rating,

        lead(rating,2) over(
            partition by employee_id 
            order by review_date desc
        ) 2_prev_rating,

        rating - coalesce(lead(rating) over(
            partition by employee_id 
            order by review_date desc
        ),0) improvement,

        rating - coalesce(lead(rating,2) over(
            partition by employee_id 
            order by review_date desc
        ),0) improvement_score,

        count(review_id) over(
            partition by employee_id
        ) number_of_review,
        ranking

    from calculating_ranking
    where ranking <= 3  
),
filter_improvement as (
    select 
        employee_id, 
        name,
        improvement_score,
        ranking
    from calculating_stats
    where employee_id not in (
        select 
            employee_id 
        from calculating_stats 
        where improvement < 1
    ) 
    and number_of_review >= 3
)
select 
    employee_id, 
    name, 
    improvement_score
from filter_improvement 
where ranking <= 1
order by 3 desc, 2