# Write your MySQL query statement below
SELECT book_id, title, author, published_year FROM books
WHERE rating is NULL
ORDER BY 1