# SQLAlchemy 

- Features function-based query construction: allows SQL clauses to be built via Python functions and expressions.
- Avoid writing raw SQL. It generates SQL and Python code for you to access tables, which leads to less database-related overhead in terms of the volume of code you need to write overall to interact with your models.
- Moreover, you can avoid sending SQL to the database on every call. The SQLAlchemy ORM library features automatic caching, caching collections, and references between objects once initially loaded.

## SQLAlchemy vs psycopg2
- SQLAlchemy generates SQL statements
- psycopg2 directly sends SQL statements to the database.
- SQLAlchemy depends on psycopg2 or other database drivers to communicate with the database, under the hood.

## Layers of SQLAlchemy
1. DBAPI
2. The Dialect
3. The Connection Pool
4. The Engine
5. SQL Expressions
6. SQLAlchemy ORM (optional)

![image](images/sqla.png)

### in psql:
`# \l` List all databases on the server, their owners, and user access levels


# psycopg2 commands

Establish a connection, starting a session, begins a transaction
>```python 
> psycopg2.connect('...')
>```

Sets a cursor to begin executing commands
>```python 
> cursor = connection.cursor()
>```

# References
    Doc: https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3
    https://www.youtube.com/watch?v=1uK8RjZr8Bg&t=361s

