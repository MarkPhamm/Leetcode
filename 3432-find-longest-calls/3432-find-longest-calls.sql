# Write your MySQL query statement below
SELECT first_name, type, duration_formatted FROM
(
SELECT 
    first_name, 
    type,
    DATE_FORMAT(sec_to_time(duration), '%H:%i:%s') AS duration_formatted,
    ROW_NUMBER() OVER(PARTITION BY type ORDER BY duration DESC) AS rn
FROM Calls JOIN contacts ON Calls.contact_id = Contacts.id
) a
WHERE rn <= 3
ORDER BY 2 DESC, 3 DESC, 1 DESC