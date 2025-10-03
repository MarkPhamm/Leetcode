select a.employee_id,
count(*)overlapping_shifts 
from  EmployeeShifts a
join EmployeeShifts b
on a.employee_id=b.employee_id
and a.start_time <b.start_time 
and a.end_time>b.start_time 
group by a.employee_id
order by a.employee_id 