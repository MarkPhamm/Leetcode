# Write your MySQL query statement below
with metal as
(
    SELECT symbol from elements
    WHERE type = "Metal"
),
nonmetal as
(
    SELECT symbol from elements
    WHERE type = "Nonmetal"
)

SELECT
 metal.symbol metal,
 nonmetal.symbol nonmetal
FROM metal
JOIN nonmetal