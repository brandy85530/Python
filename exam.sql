drop database if exists exam;
create database exam default charset utf8;

use exam;

drop table if exists tb_1;

create table tb_1
(
eno   int not null comment '編號',
ename varchar(20) not null comment '學生姓名',
course   varchar(20) not null comment '科目',
score   int not null comment '學生成績',
pass  varchar(20) not null comment '是否及格',
primary key (eno)
);

insert into tb_1 values 
	(1, '小白', '數學', 80, 'pass'),
	(2, '小白', '國文', 78, 'pass'),
	(3, '小黃', '數學', 20, 'fail'),
	(4, '小黃', '國文', 56, 'fail'),
	(5, '小藍', '數學', 100, 'pass'),
	(6, '小藍', '國文', 26, 'fail');
