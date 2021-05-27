CREATE DATABASE IF NOT EXISTS hiring;

show databases;

use hiring;

create table  candidate ( name varchar(50), email varchar(50));

create table test_score ( name varchar(50), first_round int, 
second_round int, third_round int);

show tables;

insert into candidate values ('ashish', 'ashish@gmail.com');

insert into test_score values ('ashish', 7,7,7);

select * from candidate;

select * from test_score;