# sqlite

## programming sqlite

### C++

	http://www.tutorialspoint.com/sqlite/sqlite_c_cpp.htm

### python

	http://zetcode.com/db/sqlitepythontutorial/

## using REGEXP in sqlite

### from sqlite3 command prompt
we need to use the following command to load the `pcre` plugin[^2].

	1. apt-get install sqlite3-pcre
	2. Then go to sqlite3 command line "sqlite3 test.db"
	3. run the command ".load /usr/lib/sqlite3/pcre.so"
	4. test : SELECT url FROM table_name where url REGEXP '^google.*';

### from program
we can use `sqlite3_load_extension` function[^1].

[^1]: https://www.sqlite.org/c3ref/load_extension.html
[^2]: http://stackoverflow.com/questions/24037982/how-used-regexp-in-sqlite
