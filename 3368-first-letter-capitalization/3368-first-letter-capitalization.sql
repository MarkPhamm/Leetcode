WITH RECURSIVE char_split AS (
    -- Anchor: first character, position = 1
    SELECT
        content_id,
        SUBSTRING(content_text, 1, 1) AS ch,
        SUBSTRING(content_text, 2) AS remaining_text,
        1 AS pos
    FROM user_content

    UNION ALL

    -- Recursive: peel next char and increment pos
    SELECT
        content_id,
        SUBSTRING(remaining_text, 1, 1) AS ch,
        SUBSTRING(remaining_text, 2) AS remaining_text,
        pos + 1 AS pos
    FROM char_split
    WHERE remaining_text <> ''
), 
creating_upper_lower as (
    SELECT 
        content_id, 
        ch,
        pos, 
        LAG(ch) OVER(partition by content_id order by pos) prev_ch
        FROM char_split
    ORDER BY content_id, pos
),
correcting_case as (
select 
    *, 
    case 
        when prev_ch is null or prev_ch = " " then upper(ch)
        else lower(ch)
    end as correct_ch
from creating_upper_lower
)

SELECT
    content_id,
    GROUP_CONCAT(ch ORDER BY pos SEPARATOR '') AS  original_text,
    GROUP_CONCAT(correct_ch ORDER BY pos SEPARATOR '') AS converted_text
FROM correcting_case
GROUP BY content_id
ORDER BY content_id;