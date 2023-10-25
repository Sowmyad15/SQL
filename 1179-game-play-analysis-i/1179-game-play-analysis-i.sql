# Write your MySQL query statement below
with rnk_activity as(select player_id,event_date,rank() over(partition by player_id order by event_date asc) as rnk
from Activity)
select player_id,event_date as first_login from rnk_activity
where rnk=1;
