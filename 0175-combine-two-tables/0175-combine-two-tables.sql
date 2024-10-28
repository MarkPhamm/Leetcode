# Write your MySQL query statement below
select firstName, lastName, city, state from person 
left join Address
using(personID)