## 查询

### 创建数据库及表

```sql
-- 创建数据库
create database python_test default charset=utf8mb4;
-- 使用数据库
use python_test;
-- 查看正在使用的数据库
select database();

-- student表
create table students(
	id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit default 0
);

-- classes表
create table classes(
	id int unsigned primary key auto_increment not null,
    name varchar(30) not null
);

-- 查看表详情
show create table students;
```

### 创建数据库用户(不用使用root账户)

```sql
create user bione identified by '123456';
grant all on python_test.* to "bione'@'%";
flush privileges
```

说明：

+ 第1句：创建用户账户bione，密码123456 (由identified by 设置)
+ 第2句：授权python_test数据库下所有表(python_test.*) 的所有权限（all）给用户bione 在任何ip访问数据库的时候（"bione'@'%"）
+ 第3句：刷新生效用户权限

### 数据准备

```sql
-- 向students表中插入数据
insert into students values
(0,'小明',18,180.00,2,1,0),
(0,'小月月',18,180.00,2,2,0),
(0,'彭于晏',29,185.00,1,1,0),
(0,'刘德华',59,175.00,1,2,1),
(0,'黄蓉',38,160.00,2,1,0),
(0,'凤姐',28,150.00,4,2,1),
(0,'王祖贤',18,172.00,2,1,1),
(0,'周杰伦',36,NULL,1,1,0),
(0,'程坤',27,181.00,1,2,0),
(0,'刘亦菲',25,166.00,2,2,0),
(0,'金星',33,162.00,3,3,1),
(0,'静香',12,180.00,2,4,0),
(0,'郭靖',12,170.00,1,4,0),
(0,'周杰',34,176.00,2,5,0);

-- 向classes表中插入数据
insert into classes values (0,'python_01期'),(0,'python_02期');
```

### 查询基础使用

```sql
-- 查询
	-- 查询所有字段
	-- select * from 表名;
select * from students;

	-- 查询指定字段
	-- select 列1，列2... from 表名;
select id,name,age from students;

	-- 使用 as 给字段起别名
	-- select 字段 as 名字... from 表名;
select name as aa from students;

	-- select 表名.字段... from 表名;
select students.id,students.name from students;

	-- 通过as 给表起别名
	-- select 别名.字段... from 表名 as 别名;
select aa.id,aa.name from students as aa;

	-- 消除重复行
	-- distinct 字段
select distinct gender from students;
	
-- 条件查询
	-- 比较运算
	-- select ... from 表名 where ...
	-- 查询大于18岁的信息
select * from students where age>18;
	
	-- 查询小于18岁的信息
select * from students where age<18;

	-- 查询小于或者等于18岁的信息
select * from students where age<=18;

	-- 查询年龄为18岁的所有学生的名字
select name from students where age=18;
	-- != 或者 <>
	

-- 逻辑运算符
	-- and
	-- 18到28之间的所有学生信息
select * from students where age<18 and age<18;

	-- 18岁以上的女性
select * from students where age>18 and gender=2;
	
	-- or
	-- 18以上或者身高高过180(包括)以上
select * from students where age>18 or height>=180;
	
	-- not 
	-- 不在 18岁以上的女性 这个范围内的信息
select * from students where not age>18 and gender=2;	#这个是有问题的
select * from students where not (age>18 and gender=2);

	-- 年龄不是小于或者等于18 并且是女性
select * from students where (not age<=18) and gender=2;

-- 模糊查询
	-- like
	-- % 替换1个或者多个
	-- _ 替换1个
	-- 查询姓名中 以“小” 开始的名字
select name from students where name like "%小%";

	-- 查询有2个字的名字
select name from students where name like "__";

	-- 查询有3个字的名字
select name from students where name like "___";

	-- 查询至少有2个字的名字 
select name from students where name like "__%";

	-- rlike 正则
	-- 查询以 周开始的姓名
select name from students where name rlike "^周.*";

	-- 查询以 周开始，伦结尾的姓名
select name from students where name rlike "^周.*伦$";
	
-- 范围查询
	-- in（1,3,8）表示在一个非连续的范围内
	-- 查询 年龄为18，34的姓名
select name,age from students where age in (18,34);

	-- not in 不非连续的范围之内
	-- 年龄不是 12，18，34岁之间的信息
select name,age from students where age not in (12,18,34);

	-- between ...and... 表示在一个连续的范围内
	-- 查询 年龄在18到34之间的信息
select name,age from students where age between 18 and 34;
	-- not between...and... 表示不在一个连续的范围内
	-- 查询 年龄不在18到34之间的信息
select name,age from students where age not between 18 and 34;
select name,age from students where not age (between 18 and 34);	#错误的
-- 空判断
	-- 判断 is null
	-- 查询身高为空的信息
select * from students where height is null;

	-- 判断非空is not null
select * from students where height is not null;


```

##### 排序

```sql
-- 排序
	-- order by 字段
	-- asc从小到大排序，即升序
	-- desc从大到小的排序，即降序
	
	-- 查询年龄在18到34岁之间的男性，按照年龄从小到到排序
select * from students where (age between 18 and 34) and gender=1 order by age;

	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序
select * from students where (age between 18 and 34) and gender=2 order by -height;

	-- order by 多个字段
	-- 查询年龄在18到34之间的女性，身高从高到矮排序，如果身高相同的情况下年龄从小到大排序
select * from students where (age between 18 and 34) and gender=2 order by height desc,age asc;

	-- 查询年龄在18到34之间的女性，身高从高到矮排序，如果身高相同的情况下年龄从小到大排序
	-- 如果年龄也相同那么按照id从大到小排序
select * from students where (age between 18 and 34) and gender=2 order by height desc,age asc,id desc;

	-- 按照年龄从小到大，身高从高到矮排序
select * from students order by age asc,height desc;
```

##### 聚合函数

```sql
-- 聚合函数
	-- 总数
	-- count
	-- 查询男性有多少人，女性有多少ren
select count(*) as 女性人数 from students where gender=1;

	-- 最大值
	-- max
	-- 查询最大的年龄
select max(age) from students;

	-- 查询女性的最高 身高
select max(height) from students where gender=1;

	-- 最小值
	-- min
select min(age) from students;

	-- 求和 sum
	-- 计算所有人的年龄
select sum(age) from students;

	-- 平均值 avg
	-- 计算平均年龄
select avg(age) as 平均年龄 from students;

	-- 计算平均年龄 sum(age)/count(*)
select sum(age)/count(*) from students;

	-- 四舍五入 round(123.23, 1) 保留1位小数
	-- 计算所有人的平均年龄，保留2位小数
select round(avg(age),2) as 平均年龄 from students;

select round(avg(height),2) from students where gender=1;
-- 分组
	-- group by
	-- 按照性别分组，查询所有性别
 select gender from students group by gender;
	
	-- 计算每种性别中的人数
 select gender,count(*) from students group by gender;
 
	-- 计算男性的人数
select gender,count(*) from students where gender=1 group by gender;

	-- ground_concat(..)
	-- 查询同种性别中的姓名
select gender,group_concat(name) from students group by gender;

 select gender,group_concat(name, "_", age) from students where gender=1 group by gender;
 
	-- having
	-- 查询平均年龄超过30岁的性别，以及姓名 having avg(age)>30
select gender,group_concat(name),avg(age) from students group by gender having avg(age) >30;

	-- 查询每种性别中的人数多余2个的信息
select gender,group_concat(name) from students group by gender having count(*)>2;

-- 分页
	-- limit start， count	# limit(第N页-1)*每个的个数，每页的个数
	-- 查询前5个数据
select * from students limit 0,5;
	-- 查询id6-10（包含）的书序
select * from students limit 5,5;
	-- 每页显示2个，第1个页面
select * from students limit 0,2;
	-- 每页显示2个，第2个页面
select * from students limit 2,2;	
	-- 每页显示2个，显示第6页的信息，按照年龄从小到大排序
	
	
```

##### 连接查询

```sql
-- 连接查询
	-- inner join ... on
	select * from students inner join classes;
	-- 查询 有能够对应班级的学生以及班级信息
select * from students inner join classes on students.cls_id=classes.id;

	-- 按照要求显示姓名、班级
select students.*,classes.name from students inner join classes on students.cls_id=classes.id;

select students.name,classes.name from students inner join classes on students.cls_id=classes.id;

	-- 给数据表起名字
select s.name,c.name from students as s inner join classes as c on s.cls_id=c.id;

	-- 查询 有能够对应班级的学生以及班级信息，显示学生的所有信息，只显示班级名称
select s.*,c.name from students as s inner join classes as c on s.cls_id=c.id;
	
	-- 在以上的查询中，将班级姓名显示在第1列
select c.name,s.*from students as s inner join classes as c on s.cls_id=c.id;

	-- 查询 有能够对应班级的学生以及班级信息，按照班级进行排序
select c.name,s.*from students as s inner join classes as c on s.cls_id=c.id order by c.name;
	-- 当同一个班级的时候，按照学生的id进行从小到大排序
select c.name,s.*from students as s inner join classes as c on s.cls_id=c.id order by c.name,s.id;

	-- left join	表示以左边表为基准，
	-- 查询每个学生对应的班级信息
select * from students as s left join classes as c on s.cls_id=c.id;

	-- 查询没有对应的班级信息的学生
select * from students as s left join classes as c on s.cls_id=c.id having c.id is n;

	-- right join...on
	-- 将数据表名字互换位置，用left join完成
	
```

##### 自关联

+ 创建areas表

```sql
create tables areas(
	aid int primary key,
	atitle varchar(20),
	pid int
);
```

+ 插入sql数据

> 在areas.sql文件所在位置进入终端，并进入mysql，选择python_test数据库，查看有没有新建的表areas

```sql
# z
source areas.sql;
```



