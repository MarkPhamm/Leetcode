# Write your MySQL query statement below
with recursive feb_data as (
    select * from Tweets 
    where tweet_date between '2024-02-01' and '2024-02-29'
),

base as (
    select 
        tweet_id,
        1 as pos,
        substring_index(tweet, ' ', 1) c,
        substring(tweet, length(substring_index(tweet, ' ', 1)) + 2) remain
    from feb_data 

    union all 

    select 
        tweet_id,
        pos+1 as pos,
        substring_index(remain, ' ', 1) c,
        substring(remain, length(substring_index(remain, ' ', 1)) +2) remain
    from base
    where length(remain) > 0 
)

select 
    c as hashtag,
    count(distinct tweet_id) count
from base 
where left(c,1) = '#'
group by 1 
order by 2 desc , 1 desc 
limit 3

-- select * from base
-- where tweet_id = 2
-- where c = '#HappyDay'


-- | user_id | tweet_id | tweet_date | tweet                                                                       |
-- | ------- | -------- | ---------- | --------------------------------------------------------------------------- |
-- | 100     | 1        | 2024-02-01 | Learning something new every day #Fitness #Learning #TechLife               |
-- | 101     | 2        | 2024-02-29 | What a beautiful day it is #HappyDay #WorkLife #Fitness                     |
-- | 102     | 3        | 2024-02-07 | What an amazing meal #TechLife #WorkLife                                    |
-- | 103     | 4        | 2024-02-19 | So grateful for today's experiences #HappyDay #Fitness                      |
-- | 104     | 5        | 2024-02-14 | What an amazing meal #Travel                                                |
-- | 105     | 6        | 2024-02-18 | Exploring new places and loving it #Nature #Fitness                         |
-- | 106     | 7        | 2024-02-06 | Traveling, exploring, and living my best life #Travel #Fitness              |
-- | 107     | 8        | 2024-02-29 | What a beautiful day it is #TechLife #HappyDay #Travel                      |
-- | 108     | 9        | 2024-02-13 | Exploring new places and loving it #Nature #Travel                          |
-- | 109     | 10       | 2024-02-09 | Exploring new places and loving it #Foodie #WorkLife #TechLife              |
-- | 110     | 11       | 2024-02-20 | Work hard, play hard, and cherish every moment #WorkLife #Learning #Fitness |
-- | 111     | 12       | 2024-02-12 | So grateful for today's experiences #Nature #HappyDay #Learning             |
-- | 112     | 13       | 2024-02-05 | Traveling, exploring, and living my best life #Foodie                       |
-- | 113     | 14       | 2024-02-06 | Exploring new places and loving it #Fitness #TechLife #Foodie               |
-- | 114     | 15       | 2024-02-07 | So grateful for today's experiences #TechLife #HappyDay                     |