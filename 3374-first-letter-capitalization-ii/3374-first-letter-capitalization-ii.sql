-- idea: split the char into mulitple row using recursive cte
-- lead to find the prev char, if it's '-' than use upper on that else lower
-- combine it back using group_concat 
-- hello world of SQL  
-- base case:
--    content_id: 1
--    pos: 1
--    char: h
--    remaining: ello world of SQL
-- recursion 1: 
--    content_id: 1
--    pos: 1+1 = 2
--    char: e
--    remaining: llo world of SQL


-- | content_id | pos | ch  | remaining                      |
-- | ---------- | ------- | --- | ------------------------------ |
-- | 1          | 1       | h   | ello world of SQL              |
-- | 1          | 2       | e   | llo world of SQL               |
-- | 1          | 3       | l   | lo world of SQL                |
-- | 1          | 4       | l   | o world of SQL                 |
-- | 1          | 5       | o   |  world of SQL                  |
-- | 1          | 6       | " " | world of SQL                   |
-- | 1          | 7       | w   | orld of SQL                    |
-- | 1          | 8       | o   | rld of SQL                     |
-- | 1          | 9       | r   | ld of SQL                      |
-- | 1          | 10      | l   | d of SQL                       |
-- | 1          | 11      | d   |  of SQL                        |
-- | 1          | 12      | " " | of SQL                         |
-- | 1          | 13      | o   | f SQL                          |
-- | 1          | 14      | f   |  SQL                    ...
with recursive base as (
    select 
        content_id, 
        1 as pos, 
        substring(content_text,1,1) as ch, 
        substring(content_text,2) as remaining 
    from user_content

    union all 

    select 
        content_id, 
        pos + 1 as pos,
        substring(remaining,1,1) as ch,
        substring(remaining,2) as remaining
    from base 
    where length(remaining) > 0
),

creating_upper_lower as (
    select 
        content_id, 
        ch,
        pos, 
        lag(ch) over(partition by content_id order by pos) as prev_ch
    from base
    order by content_id, pos
),

correcting_case as (
    select 
        *, 
        case 
            when prev_ch is null or prev_ch = ' ' or prev_ch = '-' then upper(ch)
            else lower(ch)
        end as correct_ch
    from creating_upper_lower
)

select
    content_id,
    group_concat(ch order by pos separator '') as original_text,
    group_concat(correct_ch order by pos separator '') as converted_text
from correcting_case
group by content_id
order by content_id