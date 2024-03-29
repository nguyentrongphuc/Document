# SQLAlchemy 

- Features function-based query construction: allows SQL clauses to be built via Python functions and expressions.
- Avoid writing raw SQL. It generates SQL and Python code for you to access tables, which leads to less database-related overhead in terms of the volume of code you need to write overall to interact with your models.
- Moreover, you can avoid sending SQL to the database on every call. The SQLAlchemy ORM library features automatic caching, caching collections, and references between objects once initially loaded.
- python document: https://peps.python.org/pep-0008/

## SQLAlchemy vs psycopg2
- SQLAlchemy generates SQL statements
- psycopg2 directly sends SQL statements to the database.
- SQLAlchemy depends on psycopg2 or other database drivers to communicate with the database, under the hood.

### Installation
- `$ pip install pyscopg2`
- `pip install psycopg2-binary`

## Layers of SQLAlchemy
1. DBAPI
2. The Dialect
3. The Connection Pool
4. The Engine
5. SQL Expressions
6. SQLAlchemy ORM (optional)

![image](images/sqlalchemy-layers-of-abstraction.png)

## Engine:
### Takeaways The Engine
- 1 of 3 main layers for how you may choose to interact with the database.
- Is the lowest level layer of interacting with the database, and is much like using the DBAPI directly. Very similar to using psycopg2, managing a connection directly.

Moreover,
- The Engine in SQLAlchemy refers to both itself, the Dialect and the Connection Pool, which all work together to interface with our database.
- A connection pool gets automatically created when we create an SQLAlchemy engine.

>```python 
> from snowflake.sqlalchemy import URL
> from sqlalchemy import create_engine
> from sqlalchemy.dialects import registry
>
> engine = create_engine(URL(
>       account=snowflake.account,
>       authenticator=snowflake.authenticator,
>       user=user,
>       password=password,
>       database=database,
>       schema=schema,
>       warehouse=warehouse,
>       role=role
>   ))
> con = engine.connect()
> result = con.execute(f'Select * ...')
> row = result.fetchone()
> row = result.fatchall()
> 
> con.close()
>```

## SQL Expressions
### Takeaways
- Instead of sending raw SQL (using the Engine), we can compose python objects to compose SQL expressions, instead.
- SQL Expressions still involves using and knowing SQL to interact with the database.

>```python 
> todos = Table('todos', ...)
> ins = todos.insert().values(
>   description = 'Clean my room',
>   completed = False
> )
> s = select([todos])
> conn = engine.connect()
> result = engine.execute(ins)
> result = conn.execute(s)
>
> result.close()
>
> todos.c.description # <Column description in todos table>
>```

## ORM
![image](images/pysql.png)

## Flask and SQLAlchemy
- Flask is a Python library that offers a very simple web framework for serving web pages with data. By installing Flask, we can use Flask in a Python script is using from Flask importing a Flask class, and then use that Flask class to start creating Flask applications.
- The second library that we're using is called Flask SQL Alchemy. Flask SQL Alchemy is a Flask extension that supports the use of SQL Alchemy underneath.
- You can install Flask SQL Alchemy using pip3 or pip if you haven't linked to pip3
>```python 
> pip3 install flask
> pip3 install flask-sqlalchemy
>```

### Create web-app with Flask

- Create file: flask-hello-app.py 
>```python 
> from flask import Flask
>
> app = Flask(__name__)
> @app.route('/')
> def index():
>    return 'Hello World!'
>```

- Start the webapp by open Terminal and run:
>```terminal 
> FLASK_APP=flask-hello-app.py flask run
> * Serving Flask app 'flask-hello-app.py'
> * Debug mode: off
> WARNING: This is a development server. Do not use it in a production deployment. 
> Use a production WSGI server instead.
> * Running on http://127.0.0.1:5000
>```

- Copy and paste the link `http://127.0.0.1:5000` or `localhost:5000` to browser to see the web-application

- We run a flask app defined at app.py by running this line of code on one line
    + `FLASK_APP=app.py FLASK_DEBUG=true flask run`
    + `FLASK_APP` must be set to the server file path with an equal sign in between. No spaces. FLASK_APP = app.py will not work.
    + `FLASK_DEBUG=true` will enable debug mode which allows live reload
    + `flask run` actually executes the flask server code in the app.py file
### Connect DB
![image](images/database-connection-uri-parts.png)

>```python 
> from flask import Flask
> from flask_sqlalchemy import SQLAlchemy
>
> app = Flask(__name__)
> app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:P%40ssw0rd@localhost:5432/snowflake' # The password contains "@", you can escape the "@" character using "%40" instead.
> db = SQLAlchemy(app)
> 
> class Person(db.Model):
>   __tablename__ = 'persons'
>   id = db.Column(db.Integer, primary_key=True)
>   name = db.Column(db.String(), nullable=False)
>
> # As of Flask-SQLAlchemy 3.0, all access to db.engine (and db.session) requires an active Flask application context. 
> # db.create_all uses db.engine, so it requires an app context.
> with app.app_context():
>    db.create_all()
>
> @app.route('/')
> def index():
>    return 'Hello World!'
>```

### Secret/environment variables handling
- Database connection info needs to be handled as Environment variables; you can use the os package to create environment variables with default values.

- There is guidance available directly in the code section; To see more details and capabilities on how to handle environment variables on Python, I recommend this [StackOverflow's thread](https://stackoverflow.com/questions/4906977/how-can-i-access-environment-variables-in-python)

- Here is an example:
    + config.py
        ``` python
        import os
        # Connect to the database
        DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')  
        DB_USER = os.getenv('DB_USER', 'postgres')  
        DB_PASSWORD = os.getenv('DB_PASSWORD', 'P%40ssw0rd')  
        DB_NAME = os.getenv('DB_NAME', 'trivia')  
        DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

        # TODO IMPLEMENT DATABASE URL
        SQLALCHEMY_DATABASE_URI = DB_PATH
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        ```
    + models.py
        ```python
        from sqlalchemy import Column, String, Integer
        from flask_sqlalchemy import SQLAlchemy

        db = SQLAlchemy()

        def setup_db(app):
            app.config.from_object('config')
            db.app = app
            db.init_app(app)
            db.create_all()
        ```
    + __init__.py (app)
        ```python
        import os
        from flask import Flask, request, abort, jsonify
        from flask_sqlalchemy import SQLAlchemy
        from flask_cors import CORS
        from models import setup_db, Question, Category

        def create_app(test_config=None):
            app = Flask(__name__)
            app.app_context().push()
            setup_db(app)

            #Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
            CORS(app)
            #Use the after_request decorator to set Access-Control-Allow
            @app.after_request
            def after_request(response):
                response.headers.add(
                    "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
                )
                response.headers.add(
                    "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
                )
                return response

            @app.route("/categories")
            def retrieve_categories():
                return jsonify( { "success": True }
                )

            return app
        ```
#### Takeaways
- Given an instance of the SQLAlchemy class from Flask-SQLAlchemy,
`db = SQLAlchemy(app)`

+ `db` is an interface for interacting with our database
+ `db.Model` lets us create and manipulate data models
+ `db.session` lets us create and manipulate database transactions

## Experimenting in Interactive Mode (python3)
Use python3 from terminal to import the library
- [ ] Rename your app from `flask-hello-app.py` to `flask_hello_app.py` (replace the dashes with underscores, so that we can import it with Python)
- [ ] Go to terminal and enter Python interactive mode by entering `python3`
- [ ] Import the app by running `import flask_hello_app` (notice that there is no `.py` at the end when we are importing.)
- [ ] If you get the deprecation warning, modify the app to set `app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False`
- [ ] Try importing again - you should now get a successful import with no errors or warnings

>```Terminal 
> $ python3
> >>> from flask_hello_app import Person, db
> >>> Person.query.all()
> >>> Person.query.first()
> >>> query = Person.query.filter(Person.name == 'Amy')
> >>> query.first()
> >>> query.all()
> >>> Person.query.first().name
>
> # Other sample
> person1 = Person(name='New Person 1')
> person2 = Person(name='New Person 2')
> db.session.add_all([person1],[person2])
> db.session.commit()
>```

![image](images/python3_script.png)

## Model.query
- query
    + `MyModel.query.all()`
    + `MyModel.query.first()`
- Filtering
    + `MyModel.query.filter_by(my_table_attribute='some value')`
    + `MyModel.query.filter(MyOtherModel.some_attr='some value')`
    + `OrderItem.query.filter(Product.id=3)`
- Ordering
    + `MyModel.order_by(MyModel.created_at)`
    + `MyModel.order_by(db.desc(MyModel.created_at))`
- Limit
    + `Order.query.limit(100).all()`
- Aggregates
    + count: 
        + `query = Task.query.filter(completed=True)`
        + `query.count()`
    + get
        + `model_id = 3`
        + `MyModel.query.get(model_id)`
- Bulk Deletes
    + `query = Task.query.filter_by(category='Archived')`
    + `query.delete()`
- Join
    + `Driver.query.join('vehicles')`

## Object Lifecycle
![image](images/object_lifecycle.png)    

## db.relationship
![image](images/db_relationship.png)

![image](images/db_relationship1.png)

### Many-To-Many
- https://www.youtube.com/watch?v=17FW9tAaDvA&t=85s

>```Python
> order_items = db.Table('order_items',
>     db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
>     db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
> )
> 
> class Order(db.Model):
>   id = db.Column(db.Integer, primary_key=True)
>   status = db.Column(db.String(), nullable=False)
>   products = db.relationship('Product', secondary=order_items,
>       backref=db.backref('orders', lazy=True))
> 
> class Product(db.Model):
>   id = db.Column(db.Integer, primary_key=True)
>   name = db.Column(db.String(), nullable=False)
> ```

### Lazy loading vs. Eager loading
- https://www.youtube.com/watch?v=oq-Wqp_BSps

#### Lazy loading
Load needed joined data only as needed. Default in SQLAlchemy.
- Pro: no initial wait time. Load only what you need.
- Con: produces a join SQL call every time there is a request for a joined asset. Bad if you do this a lot.

#### Eager loading
Load all needed joined data objects, all at once.

- Pro: reduces further queries to the database. Subsequent SQL calls read existing data
- Con: loading the joined table has a long upfront initial load time.

`lazy=True` (lazy loading) is the default option in `db.relationship`:

`children = db.relationship('ChildModel', backref='some_parent', lazy=True)`

#### Other loading options:
- https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html
- https://www.youtube.com/watch?v=qywsiQi6lvk&t=54s


### resources:
- https://www.youtube.com/watch?v=QATpsBELc8s
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#simple-relationships
- https://docs.sqlalchemy.org/en/20/orm/relationship_api.html#sqlalchemy.orm.relationship


# References
- SQL Expressions: https://www.youtube.com/watch?v=HBH0b5n7bpU&t=108s
- Mapping between Tables and Classes: https://www.youtube.com/watch?v=CF_tkEnIv44&t=128s
- Flask: https://www.youtube.com/watch?v=YbJKcTt_Gd8&t=234s
- Declaring Models: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
- Summary: https://www.youtube.com/watch?v=mueAE7foF7o&t=81s
