# mysql usage

## create databases

http://www.wikihow.com/Create-a-Database-in-MySQL


## create table

```
CREATE table <table_name>(column1 data_type,
    column2 data_type,
    ...
    PRIMARY KEY( one or more columns )
    );
```

## delete table


```
drop table <tablename>
```


## delete table entries

```
delete from <table_name> where ....
```

## get all the tables

```
select * from information_schema.tables
```

## get information about a table

```
describe <tablename>
```

## show the columns of a table

```
describe table_name;
```

## modify a table

### add a column

```
alter table <table_name> add <column_name> <datatype>
```

### change a column

```
ALTER TABLE <table_name> MODIFY COLUMN <column_name> <datatype>
```

[^1]: http://www.w3schools.com/sql/sql_alter.asp
[^2]: https://www.tutorialspoint.com/sql/sql-drop-table.htm
