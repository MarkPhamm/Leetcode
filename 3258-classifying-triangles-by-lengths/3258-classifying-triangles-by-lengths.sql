# Write your MySQL query statement below

SELECT
    CASE
        WHEN A+B<=C OR B+C<=A OR A+C <=B THEN "Not A Triangle"
        ELSE 
            CASE 
                WHEN A=B AND B=C AND C=A THEN "Equilateral"
                WHEN A=B OR B=C OR C=A THEN "Isosceles"
                ELSE "Scalene"
            END
    END AS triangle_type
FROM Triangles