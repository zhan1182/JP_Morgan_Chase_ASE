## This project builds a trading system for JP Morgan Chase in ASE 4156 course.

### Set up the system
1. Install django
2. Install MySQL and python-mysqldb
  * sudo apt-get build-dep python-mysqldb
  * pip install MySQL-python
3. Create a database in MySQL
4. Touch MySQL configure file named "my.cnf" as the following:
```
[client]
database=<the dabase name you created>
user=<our mysql username>
password=<your mysql password>
default-character-set=utf8
```

