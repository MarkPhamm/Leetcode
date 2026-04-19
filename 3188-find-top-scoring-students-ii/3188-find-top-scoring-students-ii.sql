# Write your MySQL query statement below

# gina lam cau nay

# student doesn't maintain and average gpa > 5

-- with low_gpa_student as (
--     select 
--         student_id
--     from enrollments 
--     where gpa < 2.5

-- ),

-- with all_ranking as (
--     select
--         student_id, 
--         gpa, 
--         rank() over(partition by student_id order by course_id desc) rnk 
--     from enrollments
--     where student_id = 2
-- ),
-- low_gpa_student as (
--     select * from all_ranking
--     where rnk = 1 
--     and gpa < 2.5
-- ),

with low_gpa_student as (
    select student_id from enrollments
    group by 1 
    having avg(gpa) < 2.5
),

all_courses_need as (
    select 
        student_id, 
        major as student_major, 
        course_id, 
        mandatory
    from students
    join courses
    using(major)
),

all_enrollment as (
    select 
        student_id, 
        courses.major as course_major , 
        course_id, 
        grade
    from enrollments 
    join students
    using(student_id)
    left join courses
    using(course_id)
),

join_expected_enrollment_to_reality as (
    select 
        all_courses_need.student_id, 
        all_courses_need.course_id,
        course_major, 
        student_major, 
        grade, 
        mandatory 

    from all_courses_need
    left join all_enrollment
    using(student_id, course_id) 
), 

missing_mandatory_courses as (
    select
        student_id
    from join_expected_enrollment_to_reality
    where mandatory = 'yes'
    and grade is null 
),

missing_elective_course as (
    select 
        student_id 
    from join_expected_enrollment_to_reality
    where mandatory = 'no'
    group by 1 
    having count(grade) <= 1 
), 

missing_grade_citeria as (
    select 
        distinct student_id 
    from join_expected_enrollment_to_reality 
    where (mandatory = 'yes' and grade != 'A')
    or (mandatory = 'No' and grade not in  ('A', 'B'))
)


select 
    distinct 
        student_id 
from students
where student_id not in (select student_id from low_gpa_student)
and student_id not in (select student_id from missing_mandatory_courses)
and student_id not in (select student_id from missing_elective_course)
and student_id not in (select student_id from missing_grade_citeria)

-- select * from enrollments 
-- right join courses 
-- using(course_id) 
-- join students 
-- using(student_id)
-- where student_id = 8  

-- | student_id | course_id | name                 | credits | major                  | mandatory | semester | grade | GPA | name  | major     |
-- | ---------- | --------- | -------------------- | ------- | ---------------------- | --------- | -------- | ----- | --- | ----- | --------- |
-- | 8          | 1         | Software Engineering | 4       | Economics              | no        | Spring   | B     | 2.2 | Grace | Chemistry |
-- | 8          | 2         | Linear Algebra       | 3       | Economics              | no        | Fall     | A     | 2.5 | Grace | Chemistry |
-- | 8          | 4         | Database Systems     | 4       | Economics              | no        | Spring   | B     | 2.9 | Grace | Chemistry |
-- | 8          | 6         | Data Structures      | 4       | Mechanical Engineering | yes       | Spring   | A     | 3   | Grace | Chemistry |
-- | 8          | 7         | Algorithms           | 1       | Mechanical Engineering | no        | Spring   | B     | 3.1 | Grace | Chemistry |
-- | 8          | 8         | Calculus             | 3       | Chemistry              | yes       | Fall     | A     | 2.9 | Grace | Chemistry |
-- | 8          | 9         | Algorithms           | 2       | Chemistry              | yes       | Spring   | A     | 2.1 | Grace | Chemistry |

-- select 
--     *
-- from missing_elective_course



-- | student_id | major     | course_id | mandatory |
-- | ---------- | --------- | --------- | --------- |
-- | 8          | Chemistry | 8         | yes       |
-- | 8          | Chemistry | 9         | yes       |
-- | 8          | Chemistry | 10        | no        |
-- | 8          | Chemistry | 11        | no        |
