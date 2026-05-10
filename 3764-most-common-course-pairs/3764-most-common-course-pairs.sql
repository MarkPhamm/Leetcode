# Write your MySQL query statement below
-- Consider only top-performing students (those who completed at least 5 courses with an average rating of 4 or higher).
-- For each top performer, identify the sequence of courses they completed in chronological order.
-- Find all consecutive course pairs (Course A → Course B) taken by these students.
-- Return the pair frequency, identifying which course transitions are most common among high achievers.


with top_performing_students as (
    select 
        user_id
    from course_completions 
    group by 1
    having count(course_id) >= 5
    and avg(course_rating) >= 4
),

calc_next_course as (
    select 
        user_id, 
        course_name, 
        completion_date, 
        lead(course_name) over(partition by user_id order by completion_date) next_course
    from course_completions
    where user_id in (select * from top_performing_students)
)

select 
    course_name first_course, 
    next_course second_course,
    count(user_id) transition_count
from calc_next_course
where next_course is not null
group by 1,2 
order by 3 desc, 1, 2