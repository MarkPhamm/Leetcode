# Write your MySQL query statement below
-- with agg as (
--     select 
--     ip, 
--     count(*) as invalid_count,
--     SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 1), '.', -1) first,
--     SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) second,
--     SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) third,
--     SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 4), '.', -1) forth,
--     LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) AS dot_count
--     from logs
--     group by 1
-- ),
-- splitting_string as (
--     select 
--     *,
--     case 
--         when dot_count != 3 then 'invalid'
--         when dot_count = 3 then 
--             case 
--                 when left(first,1) = '0' or left(second,1) = '0' or left(third,1) = '0' or left(forth,1) = '0' then 'invalid'
--                 when cast(first as unsigned) > 255 or cast(second as unsigned) > 255 or cast(third as unsigned) > 255 or cast(forth as unsigned) > 255 then 'invalid'
--             end
--         else 'valid'
--     end status
--     from agg
-- )
-- select 
--     ip, 
--     invalid_count
-- from splitting_string 
-- where status = 'invalid'
-- order by invalid_count desc, ip desc


SELECT 
    ip,
    count(*) invalid_count
FROM logs
WHERE ip NOT REGEXP '^(?:[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:[.](?:[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$'
GROUP BY 1
ORDER BY 2 desc, 1 desc 