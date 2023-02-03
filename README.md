## Todo website

This is a very simple website to manage a TODO list with five priorities. It is rudimentary, simple, does not use any special fonts or Javascript, only Python on a webserver.

In other words, I have been using this humble LAMP project as my personal TODO list and have been very happy with it.

### It is a LAMP project:
- Linux = Raspberry Pi OS
- Apache = Apache2
- Mysql = MariaDB
- PHP/Perl/Python = Python

### HOWTO
There are stars from * till *****. For me ***** is the most urgent TODO and * is the least urgent. YMMV
![todo1](https://user-images.githubusercontent.com/524195/198712930-b702fa3d-ba50-43f6-8730-540c1a0d8adf.png)



The arrow symbols next to an item can be used to move the item left or right.
![todo2](https://user-images.githubusercontent.com/524195/198713130-cfc3c873-6665-4aa5-9dad-c9f7a04d0f1d.png)



The formfield can be used to add an item (with a priority).
![todo4](https://user-images.githubusercontent.com/524195/198713264-148fdf6c-563d-40be-b0a5-9ed5364422e4.png)



The check mark (granted it is a square root symbol) next to an item can be used to 'delete' the item. Delete items are moved to the 'Done' table below.
![done2](https://user-images.githubusercontent.com/524195/198713725-9746675e-7b00-487c-8b93-fa9ed6e388a1.png)



Items can be purged from 'Done' using the circle_with_cross symbol.
![purge](https://user-images.githubusercontent.com/524195/198713774-19a02049-367e-4d4d-bf37-1bda76d06bb2.png)


### installing
Installing may require these steps:
- apt install apache2 libapache2-mod-python mariadb-server
- pip3 install mysql-connector-python
- add .py as handler in /etc/apache/mods-enabled/mime.conf
- cp index.py /var/www/html/
- create database todo;
- create table todo (item varchar(255), priority enum('1','2','3','4','5'), done tinyint(1), date date);
- insert into todo values ('test','2',0, '2023-02-02');

### BUGS
- There is no unique key in the table, so identical items are 'deleted' together.
- There is no update on the URL so a refresh will create a double item.
- I don't care about these bugs, sorry.

### root/hunter2
This code contains the root user with password 'hunter2'. I remember reading somewhere [http://bash.org/?244321] that it is the most secure password in the world, so I use it everywhere.

### LICENSE
Consider this public domain.
Nice people quote the source somewhere.
