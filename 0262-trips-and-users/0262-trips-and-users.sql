
SELECT request_at as 'Day',
ROUND((COUNT(CASE WHEN status like 'cancelled%' then 1 else null end)/COUNT(*)),2) as 'Cancellation Rate'
FROM TRIPS
WHERE client_id not in
(
  SELECT users_id from Users
  where banned = 'Yes'
)
AND driver_id not in
(
  SELECT users_id from Users
  where banned = 'Yes'
)
AND request_at between "2013-10-01" and "2013-10-03"
GROUP BY 1