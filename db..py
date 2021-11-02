import sqlite3

con=sqlite3.connect("Details.db")

print("Database Created")

con.execute("create table users(ID integer primary key autoincrement,Name varchar(20) not null,Lastname varchar(20) not null,EmailID varchar(25) not null,Age int not null,Place varchar(15) not null,Password varchar(15) not null)");
print("Table Created Successfully")