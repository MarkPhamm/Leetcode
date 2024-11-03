# Write your MySQL query statement below

WITH secondary_sales as
(

SELECT * FROM 
(
    SELECT 
    seller_id, 
    item_id,
    RANK() OVER(PARTITION BY seller_id ORDER BY order_date) ranking 
    FROM Orders
) a 
WHERE ranking = 2
)
SELECT 
    user_id as seller_id, 
    IF(favorite_brand = item_brand, 'yes', 'no') as 2nd_item_fav_brand
FROM Users
LEFT JOIN secondary_sales
ON Users.user_id = secondary_sales.seller_id
LEFT JOIN Items
ON secondary_sales.item_id = Items.item_id
ORDER BY 2