# Write your MySQL query statement below
-- A Study Spiral Pattern means a student studies at least 3 different subjects in a repeating sequence
-- The pattern must repeat for at least 2 complete cycles (minimum 6 study sessions)
-- Sessions must be consecutive dates with no gaps longer than 2 days between sessions
-- Calculate the cycle length (number of different subjects in the pattern)
-- Calculate the total study hours across all sessions in the pattern
-- Only include students with cycle length of at least 3 subjects
with base as (
    select
        *, 
        row_number() over(partition by student_id, subject order by session_date) spiral_id 
    from study_sessions
),
calc_prev_session_time as (
    select 
        *,
        lag(session_date) over(partition by student_id, subject order by spiral_id)  prev_same_subject_session_date,
        lag(session_date) over(partition by student_id order by session_date)  prev_session_date,
        datediff(session_date, 
        lag(session_date) over(partition by student_id order by session_date)) as diff 
    from base 
), 
subject_group_agg as (
    select 
        student_id,
        spiral_id, 
        group_concat(subject order by session_id) as subject_group,
        count(distinct subject) cycle_length,
        sum(hours_studied) hours_studied
    from calc_prev_session_time
    where diff <= 2 or diff is null 
    group by 1,2
    having count(distinct subject) >= 3 
),
filter_more_than_two_cycle as (
    select 
        student_id, 
        subject_group, 
        cycle_length, 
        sum(hours_studied) total_study_hours,
        count(*)
    from subject_group_agg
    group by 1,2,3
    having count(*) >= 2
)

select 
    student_id, 
    student_name,
    major, 
    cycle_length, 
    total_study_hours
from filter_more_than_two_cycle
join students using(student_id)
order by cycle_length desc, total_study_hours desc 
-- select * from calc_prev_session_time 