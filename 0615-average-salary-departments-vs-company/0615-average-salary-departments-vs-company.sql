# Write your MySQL query statement below

SELECT distinct 
    DATE_FORMAT(pay_date, "%Y-%m") as pay_month,
    department_id,
    CASE 
        WHEN 
            AVG(amount) OVER(partition by DATE_FORMAT(pay_date, "%Y/%m")) = 
            AVG(amount) OVER(partition by DATE_FORMAT(pay_date, "%Y/%m"), department_id)
        THEN "same"
        WHEN 
            AVG(amount) OVER(partition by DATE_FORMAT(pay_date, "%Y/%m")) > 
            AVG(amount) OVER(partition by DATE_FORMAT(pay_date, "%Y/%m"), department_id)
        THEN "lower"
        ELSE
            "higher"
    END as comparison  
FROM Salary
JOIN Employee 
USING(employee_id)