# Write your MySQL query statement below

WITH toppings_cte AS
(
SELECT 
    DISTINCT *,
    ROW_NUMBER() OVER(ORDER BY topping_name) rnk 
FROM Toppings
)
SELECT 
    CONCAT(first.topping_name, ",",
    second.topping_name, ",",
    third.topping_name) pizza           ,
    first.cost + second.cost + third.cost total_cost 
FROM toppings_cte first
JOIN toppings_cte second ON first.rnk < second.rnk
JOIN toppings_cte third ON second.rnk < third.rnk
ORDER BY total_cost DESC, pizza