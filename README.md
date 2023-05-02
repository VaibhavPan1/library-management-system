# library-management-system

pip install Pillow
pip install pymysql
pip install cryptography


Do this before opening project:
1. install mysql
2. create databse db
NOTE: you can choose any database name according to your will. If changed then update the database name if every file

3. execute this command in mysql command line:

create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));

4. execute this command in mysql command line:

create table books_issued(bid varchar(20) primary key, issuedto varchar(30));

5. change the database password in all source files.


***install other requirements as required***

For feedback and ideas, mail me at vaibhavadg123@gmail.com

