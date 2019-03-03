# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

select min(doctor), min(prof), min(singer), min(actor) from
(select RANK() OVER (PARTITION BY Occupation ORDER BY Name) as Rank,
case when Occupation='Doctor' then Name else null end as doctor,
case when Occupation='Professor' then Name else null end as prof,
case when Occupation='Singer' then Name else null end as singer,
case when Occupation='Actor' then Name else null end as actor from Occupations)
group by Rank order by min(doctor), min(prof), min(singer), min(actor);