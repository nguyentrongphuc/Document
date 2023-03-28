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

# psycopg2 commands

Establish a connection, starting a session, begins a transaction
>```python 
> psycopg2.connect('...')
>```

Sets a cursor to begin executing commands
>```python 
> cursor = connection.cursor()
>```

>```python 
> cursor.execute(<sql command string>)
> cursor.commit()
> cursor.rollback()
> # Example
> cursor.execute('SELECT * from table2;')
> result = cursor.fetchall()
> print(result)
> 
> cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))
> # Example insert with data parameters
> SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
> data = {
>   'id': 2,
>   'completed': False
> }
> cursor.execute(SQL, data)
> cursor.execute('SELECT * from table2;')
> result2 = cursor.fetchone()
> print('fetchone ' , result2)
> result = cursor.fetchmany(2)
> print('fetchmany ' , result2)
> 
> result3 = cursor.fetchone()
> print('fetchone ' , result3)
>```

# References
    Doc: https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3
    https://www.youtube.com/watch?v=1uK8RjZr8Bg&t=361s

