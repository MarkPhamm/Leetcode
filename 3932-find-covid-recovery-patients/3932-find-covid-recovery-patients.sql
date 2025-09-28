# Write your MySQL query statement below


 
with calculating_first_pos_date as (
    select 
        patient_id,
        min(test_date) first_pos_date
    from covid_tests
    where result = 'Positive'
    group by 1
),

remove_neg_results_before_first_pos as (
    select 
        covid_tests.*
    from covid_tests 
    join calculating_first_pos_date
    on covid_tests.patient_id = calculating_first_pos_date.patient_id
    and covid_tests.test_date >= calculating_first_pos_date.first_pos_date
),

creating_rnk as (
    select 
        *,
        rank() over(partition by patient_id, result order by test_date) rnk
    from remove_neg_results_before_first_pos
), 
concat_date as (
    select 
        patient_id, 
        group_concat(case when rnk = 1 and result = 'positive' then test_date else null end) as first_positive,
        group_concat(case when rnk = 1 and result = 'negative' then test_date else null end) as first_negative
    from creating_rnk
    group by 1
)
select 
    patient_id, 
    patient_name, 
    age, 
    datediff(first_negative, first_positive) as recovery_time
from concat_date
join patients 
using (patient_id)
where first_positive is not null and first_negative is not null
order by recovery_time, patient_name
