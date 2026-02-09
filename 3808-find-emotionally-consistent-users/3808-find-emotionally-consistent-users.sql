with filter_5 as (
    select
        user_id,
        count(*) as total_reaction
    from reactions
    group by user_id
    having count(*) >= 5
), 

calc_proportion as (
    select 
        user_id,
        reaction dominant_reaction,  
        round((count(content_id)*1.0)/max(total_reaction),2) reaction_ratio
    from filter_5 
    left join reactions
    using(user_id)
    group by 1,2
)
select * from calc_proportion 
where reaction_ratio >= 0.6 
order by reaction_ratio desc, user_id