# POSTGRES commands

## connect db
    psql <dbname> --username=postgres

## Useful basic psql commands
`psql <dbname> [<username>]` : Starts psql with a connection to dbname. Optionally use another user than current user

### in psql:
`# \l` List all databases on the server, their owners, and user access levels

`# \c <dbname>` Connect to a database named

`# \dt` Show database tables

`# \d <tablename>` Describe table schema

`# \q` Quit psql, return to the terminal

`# \?` Get help, see list of available commands

### table
`create table table1( id INTEGER PRIMARY KEY, description VARCHAR NOT NULL);` create table

`insert into table1(id, description) VALUES (1, 'this is a thing');` insert data into table

`select * from table1` query data from table

>```php
> id |   description   
>----+-----------------
>  1 | this is a thing
> (1 row)
>```

# References
    Doc: https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3
    https://www.youtube.com/watch?v=1uK8RjZr8Bg&t=361s
