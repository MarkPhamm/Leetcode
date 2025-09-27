# Write your MySQL query statement below
-- A book has polarized opinions if it has at least one rating ≥ 4 and at least one rating ≤ 2 (1)
-- Only consider books that have at least 5 reading sessions (2)
-- Calculate the rating spread as (highest_rating - lowest_rating)
-- Calculate the polarization score as the number of extreme ratings (ratings ≤ 2 or ≥ 4) divided by total sessions
-- Only include books where polarization score ≥ 0.6 (at least 60% extreme ratings)

select 
    book_id, 
    title,
    author,
    genre, 
    pages,
    max(session_rating) - min(session_rating) as rating_spread,  # Calculate the rating spread as (highest_rating - lowest_rating)
    round(count(case when session_rating >= 4 or session_rating <= 2 then session_id else null end)/count(session_id),2) polarization_score 
from reading_sessions
join books using(book_id)
group by 1
having count(session_id) >= 5 # Only consider books that have at least 5 reading sessions (2)
and count(case when session_rating >= 4 or session_rating <= 2 then session_id else null end)/count(session_id) >= 0.6 # Only include books where polarization score ≥ 0.6 (at least 60% extreme ratings)
and (count(case when session_rating >= 4 then session_id else null end) >= 1 and count(case when session_rating <= 2 then session_id else null end) >= 1) -- A book has polarized opinions if it has at least one rating ≥ 4 and at least one rating ≤ 2 (1)
order by polarization_score desc, title desc