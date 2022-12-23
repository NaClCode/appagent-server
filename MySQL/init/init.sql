create database if not exists appagent;
use appagent;
create table if not exists user (id int not null auto_increment,name varchar(20),password varchar(100),premission varchar(20),primary key(id));