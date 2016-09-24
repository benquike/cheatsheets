# mysql usage

## get back the root password

1. stop the mysql server

    sudo service mysql stop

2. start the mysql server in safe mode

    sudo mysqld_safe --skip-grant-tables --skip-syslog --skip-networking

3. login the mysql server and reset the passoword


    mysql -u root -p
    <password>

If the mysql server < 5.7
    UPDATE mysql.user SET Password=PASSWORD('password') WHERE User='root';
    FLUSH PRIVILEGES;

else if mysql server > 5.7

    use mysql;
    update user set authentication_string=password('password') where user='root';


## Adding new user

    CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

## granting permission to a user

    GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';

## Reference
* [How to find out the MySQL root password](http://stackoverflow.com/questions/10895163/how-to-find-out-the-mysql-root-password)
* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
