Bookshelf Application
----- 

## Tech Stack

- Flask
- Flask-CORS
- SQLAlchemy
- JSONify
- Unittest



## Pre-requisites
* Developers using this project should already have Python3, pip and node installed on their local machines.


* **Start your virtual environment** 

From the backend folder run
```bash
pip install virtualenv
python -m virtualenv env

# Mac/Linux users
source venv/bin/activate
# Windows users
source env/Scripts/activate
```

* **Install dependencies**<br>

From the backend folder run 
```bash
# All required packages are included in the requirements file. 
pip install -r requirements.txt
# In addition, you will need to UNINSTALL the following:
pip uninstall flask-socketio -y
```

## Run the Project


### Step 0: Start or Stop the PostgreSQL server

> Click [here](https://tableplus.com/blog/2018/10/how-to-start-stop-restart-postgresql-server.html) for reference.


### Step 1 - Create and Populate the database

1. **Verify the database username**<br>
Verify that the database user in the `/backend/books.psql`, `/backend/models.py`, and `/backend/test_flaskr.py` files must be either the `student` or `postgres` (default username). 

2. **Create the database and a user**<br>
In your terminal, navigate to the `backend` directory, and run the following:

```bash
cd backend

# Connect to the PostgreSQL
psql -U postgres

#View all databases
\l

# Create the database, create a user - `student`, grant all privileges to the student
\i setup.sql

# Exit the PostgreSQL prompt
\q
```


3. **Create tables**<br>
Once your database is created, you can create tables (`bookshelf`) and apply contraints,

```bash
# Mac users
psql -f books.psql -U postgres -d bookshelf

# Linux users
su - postgres bash -c "psql bookshelf < /path/to/exercise/backend/books.psql"
```

**You can even drop the database and repopulate it, if needed, using the commands above.** 


### Step 2: Start the backend server

Navigate to the `/backend/flaskr/__init__.py` file, start your (backend) Flask server by running the command below from the `/backend` directory.

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application will run on `http://127.0.0.1:5000/` by default and is set as a proxy in the frontend configuration. Also, the current version of the application does not require authentication or API keys. 



### Step 3: Start the frontend

(You can start the frontend even before the backend is up!)

From the `frontend` folder, run the following commands to start the client: 

```
npm install // only once to install dependencies
npm start 
```

By default, the frontend will run on `localhost:3000`. Close the terminal if you wish to stop the frontend server. 


---

## Additional information

#### Running Tests

If any exercise needs testing, navigate to the `/backend` folder and run the following commands:

```bash
psql postgres
dropdb bookshelf_test
createdb bookshelf_test
\q
psql bookshelf_test < books.psql
python test_flaskr.py
```