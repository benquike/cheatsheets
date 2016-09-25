# mysql usage

## get all the tables

```
select * from information_schema.tables
```

## show the columns of a table

```
describe table_name;
```

## modify a table

### add a column

```
alter table <table_name> <column_name> <datatype>
```

### change a column

```
ALTER TABLE <table_name> MODIFY COLUMN <column_name> <datatype>
```

[^1]: http://www.w3schools.com/sql/sql_alter.asp
