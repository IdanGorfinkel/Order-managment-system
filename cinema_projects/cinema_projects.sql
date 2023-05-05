use cinemaproject;


create table cinema(
			cinema_id int primary key,
            cinema_name varchar(50) ,
            street varchar(50) ,
            city varchar(50) ,
            unique(cinema_name,city));

create table theater(
			theater_number int,
            capacity int check(capacity>0),
            area float check(area>0),
            cinema_id int,
            primary key (theater_number,cinema_id),
            foreign key (cinema_id) references cinema(cinema_id));
      

create table theater_types(
			theater_number int,
            theater_type enum("2D","3D","I-MAX","VIP"),
            cinema_id int,
            primary key(theater_number,theater_type,cinema_id),
            foreign key (theater_number) references theater(theater_number),
            foreign key (cinema_id) references cinema(cinema_id));
            
create table person(
			id int primary key,
            first_name varchar (50),
            last_name varchar (50),
            phone_number varchar (50));
	
    
create table clients (
			id int primary key,
            age int,
            foreign key (id) references person(id));
            
 
create table clients_visit(
			id int,
            cinema_id int,
            visit_date date,
            primary key(id,cinema_id,visit_date),
			foreign key (id) references person(id) ,
            foreign key (cinema_id) references cinema(cinema_id));
            
create table employee (
			id int primary key,
            backup_id int not null,
            cinema_id int,
            monthly_payment int check(monthly_payment>=0),
            foreign key (id) references person(id),
            foreign key (cinema_id) references cinema(cinema_id),
            foreign key (backup_id) references employee(id));

            
create table employee_roles(
			id int,
            roles varchar(50),
            primary key(id,roles),
            foreign key (id) references person(id));
            
create table cinema_manager(
			id int primary key,
            start_date date default  "2022-01-01" ,
            cinema_id int,
            monthly_payment int check(monthly_payment>=0),
            foreign key (id) references person(id),
            foreign key (cinema_id) references cinema(cinema_id));
  
create table movie(
			movie_code int primary key,
            movie_name varchar(50) not null,
            min_age int,
            unique (movie_name));
  
  
create table movie_genre(
			movie_code int,
            genre varchar(50),
            primary key(movie_code,genre),
            foreign key (movie_code) references movie(movie_code));
            

create table broadcast(
			movie_code int,
            theater_number int,
            cinema_id int,
            primary key(movie_code,theater_number,cinema_id),
            foreign key (movie_code) references movie(movie_code),
            foreign key (cinema_id) references cinema(cinema_id),
            foreign key (theater_number) references theater(theater_number));
            
            
            

 insert into cinema (cinema_id,cinema_name,street,city)
	values
    (1,"cinema city","nez harim","shoham"),
    (2,"cinema italianno","hamaayan","tel aviv"),
    (3,"bipbapbop cinema","tel giboreem","rahat"),
    (4,"volcano cinema","bali shag","givataaym"),
    (5,"cold as ice cinema","noam","kfar yarak");
    
insert into theater (theater_number,capacity,area,cinema_id)
	values
    (10,50,150,1),
	(11,60,175,1),
    (12,100,250,1),
    (10,70,120,2),
    (11,30,90,2),
    (12,120,300,2),
    (10,50,120,3),
    (11,40,80,3),
    (12,12,60,3),
    (10,90,220,4),
    (11,25,90,4),
    (12,150,300,4),
    (10,70,120,5),
    (11,30,90,5),
    (12,75,370,5);
    
insert into theater_types(theater_number,theater_type,cinema_id)
	values
    (10,"2D",1),
	(11,"I-MAX",1),
    (12,"VIP",1),
    (10,"3D",2),
    (11,"3D",2),
    (12,"2D",2),
    (10,"I-MAX",3),
    (11,"2D",3),
    (12,"I-MAX",3),
    (10,"3D",4),
    (11,"2D",4),
    (12,"2D",4),
    (10,"3D",5),
    (11,"3D",5),
    (12,"I-MAX",5);
    
insert into person(id, first_name,last_name,phone_number)
	values
    (11111,"de","paul",05011111),
    (22222,"harry","maguire",05022222),
    (33333,"salim","toaama",05033333),
    (44444,"klinger","lo roee",05044444),
    (55555,"moti","luchim",05055555),
    (66666,"zehavi","lev adom",05066666),
    (77777,"timo","off target",05077777),
    (88888,"alvaro","offside",05088888),
    (99999,"rina","successful",05099999),
    (87777,"idan","yolo",05456643),
    (98888,"elad", "cohen",05456755),
    (99987,"yuval","foster",05234566),
    (66688,"yoav","lili",05323456),
    (44445,"zohar","liba",05234565),
    (55500,"liran","danino",05345676),
    (66654,"bar","refaeli",05234333);
    
insert into clients(id, age)
	values
    (11111,25),
    (22222,50),
    (33333,85),
    (87777,9),
    (98888,3),
    (99987,20),
    (66688,30);
    
insert into clients_visit(cinema_id, id,visit_date)
	values
    (1,33333,"2022-01-01"),
    (3,22222,"2022-02-03"),
    (1,11111,"2022-01-09"),
    (2,11111,"2016-09-09"),
    (3,11111,"2017-06-03"),
    (5,22222,"2010-02-02");
    
alter table employee drop foreign key employee_ibfk_3;

insert into employee(id, backup_id, cinema_id,monthly_payment)
	values
    (44444,55555,4,5000),
    (55555,44444,1,6000),
    (66666,77777,2,5500),
    (77777,66666,3,7000),
    (44445,66666,5,5000),
    (55500,44444,3,7000);


ALTER TABLE employee ADD FOREIGN KEY (backup_id) REFERENCES employee(id);


insert into employee_roles(id,roles)
	values
	(44444,"counter"),
    (55555,"janitor"),
    (66666,"steward"),
    (77777,"steward"),
    (44445,"counter"),
    (55500,"counter");


insert into cinema_manager(id, start_date, cinema_id, monthly_payment)
	values
    (88888,"2020-01-01",1,50000),
    (99999,"2018-01-01",2,45000),
    (66654,"2016-09-20",3,50000);
    
insert into movie(movie_code, movie_name, min_age)
	values
    (1212,"The Dark Knight",16),
    (1313,"Avatar: The Way of Water",9),
    (1414,"Terminator 2",13),
    (1515,"The Lord of the Rings",9),
    (1616,"Ballad of Narayama",4),
    (1717,"the saw",18),
	(1919,"come and see",16);
    
insert into movie_genre(movie_code,genre)
	values
    (1212,"Thriller"),
    (1313,"Fantasy"),
    (1414,"Action"),
    (1515,"Fantasy"),
    (1616,"Mystery"),
    (1717,"Horror"),
    (1919,"Horror");
    
insert into Broadcast(movie_code,theater_number, cinema_id)
	values
    (1212,10,5),
    (1313,11,4),
    (1414,10,3),
    (1515,12,1),
    (1616,11,2),
    (1717,11,3),
    (1919,12,4),
    (1212,10,3),
    (1212,12,5),
    (1313,12,1),
    (1313,10,1),
    (1414,12,1);


