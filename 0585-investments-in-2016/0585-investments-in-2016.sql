# Write your MySQL query statement below
select round(sum(tiv_2016),2)  as tiv_2016 from Insurance
where tiv_2015 in
(
select tiv_2015 from Insurance
group by 1
having count(*) >=2
) 
and concat(lat,lon) in 
(
select concat(lat,lon) from Insurance
group by 1
having count(*) = 1
)