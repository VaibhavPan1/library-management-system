# library-management-system

pip install Pillow
pip install pymysql
pip install cryptography


Do this before opening project:
1. install mysql
2. create databse db
3. execute this command in mysql command line:

create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));

4. execute this command in mysql command line:

create table books_issued(bid varchar(20) primary key, issuedto varchar(30));

5. change the database password in all source files




***satisfy other requirements as required***