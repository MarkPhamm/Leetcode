CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select IFNULL((
        select distinct(salary) from
          (
            select *, dense_rank() over(order by salary desc) ranking from Employee
          ) a
        where ranking = N),null) as getNthHighestSalary
      );
END