use cinemaproject;

select c.cinema_name,count(b.movie_code) as "Number of movies broadcast"
-- the buysiest cinema
from broadcast b, cinema c
where b.cinema_id = c.cinema_id
group by b.cinema_id
order by count(b.movie_code) desc;

select c.cinema_name,c.city, max(t.capacity) as "Capacity"
from theater t,cinema c
where t.cinema_id=c.cinema_id;


select c.cinema_name,c.city
from cinema c
where c.cinema_id in (select distinct t.cinema_id
					from theater t
					where t.capacity >100);


select p.first_name,p.last_name,er.roles,e.monthly_payment
from employee e,person p,employee_roles er
where e.id= p.id and er.id=p.id and e.monthly_payment > (select avg(monthly_payment)
														from employee);
                                                        
                                                        
select c.id ,p.first_name, p.last_name ,c.monthly_payment+1000 "new_monthly_payment"
from cinema_manager c,person p
where (2023-(extract(year from start_date)))>5 and c.id=p.id;

select cin.cinema_id, count(cl.id) "visit_amount"
from clients_visit cl, cinema cin
where extract(year from visit_date)= 2022 and cin.cinema_id=cl.cinema_id
group by cin.cinema_id;

select id, monthly_payment, cinema_id
from employee
group by monthly_payment
having monthly_payment > 5700
order by (monthly_payment)desc;

select cv.id, cv.cinema_id,count(*) 'number of visits'
from clients_visit cv, cinema c
where cv.cinema_id=c.cinema_id
group by c.cinema_id, cv.id
order by cv.id ;

select e1.id, p1.first_name, p1.last_name , e1.backup_id, 
            p2.first_name, p2.last_name
from employee e1, employee e2, person p1, person p2
where e1.id!=e2.backup_id and p1.id=e1.id and p2.id=e2.backup_id;

SELECT c.cinema_name,  m.movie_name,  count(movie_name) 
'number of times the movie brodcast in the cinema'   
FROM cinema c, broadcast b, movie m 
where c.cinema_id = b.cinema_id and b.movie_code = m.movie_code
GROUP BY  c.cinema_name,m.movie_name;

-- 2
select ci.cinema_id, cinema_name, round(avg(age)) 'the avarge age of customers'
from cinema ci, clients c, clients_visit cl, person p
where ci.cinema_id = cl.cinema_id and c.id = p.id and cl.id = p.id
group by ci.cinema_id;

-- 3
select group_concat(distinct movie_name), genre, cinema_name
from movie m, cinema c, movie_genre mg, broadcast b
where m.movie_code = mg.movie_code and m.movie_code = b.movie_code and b.cinema_id = c.cinema_id
group by min_age > 8;


