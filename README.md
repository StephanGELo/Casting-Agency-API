# Casting Agency
The name of the application is called the Casting Agency.  The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. As an Executive Producer within the company, I am motivated in creating a system to simplify and streamline the processes.

## Deployment
This app is hosted on heroku. The link to the app is https://stephangelcasting.herokuapp.com/movies.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

It is recommended working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the project directory and running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the casting.psql file provided. From the backend folder in terminal run:
```bash
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 



# https://universaleagle.auth0.com/authorize?audience=casting&response_type=token&client_id=10x7mOTvjuPIcj0jFm5Oy6cdMkLAV3CE&redirect_uri=http://127.0.0.1:5000/movies

# Testing
In order to carry out the tests on the endpoints, navigate to the backend folder in your terminal and run the following commands:

dropdb castingagency_test
createdb castingagency_test
psql castingagency_test < casting.psql
python3 test_flaskr.py


