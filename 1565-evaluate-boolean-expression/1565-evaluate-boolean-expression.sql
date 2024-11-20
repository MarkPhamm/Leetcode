# Write your MySQL query statement below

SELECT 
    left_operand, 
    operator,
    right_operand,
    CASE 
        WHEN operator = "=" THEN IF(vl.value = vr.value, "true", "false")
        WHEN operator = ">" THEN IF(vl.value > vr.value, "true", "false")
        WHEN operator = "<" THEN IF(vl.value < vr.value, "true", "false")
    END value
FROM Expressions
JOIN Variables vl ON Expressions.left_operand = vl.name
JOIN Variables vr ON Expressions.right_operand = vr.name