# Write your MySQL query statement below
select 
    book_id, 
    max(title) title, 
    max(author) author, 
    max(genre) genre, 
    max(publication_year) publication_year,
    count(case when return_date is null then record_id else null end) current_borrowers
from borrowing_records
join library_books using(book_id)
group by 1
having max(total_copies) = count(case when return_date is null then record_id else null end)
order by current_borrowers desc, title