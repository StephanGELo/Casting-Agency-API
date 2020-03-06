# Casting Agency

The name of the application is called the Casting Agency.  The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. As an Executive Producer within the company, I am motivated in creating a system to simplify and streamline the processes.

## Deployment

This app is hosted on heroku. The link to the app is [here, click me!] (https://universaleagle.auth0.com/authorize?audience=casting&response_type=token&client_id=10x7mOTvjuPIcj0jFm5Oy6cdMkLAV3CE&redirect_uri=https://stephangelcasting.herokuapp.com/movies)

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

With Postgres running, restore a database using the casting.psql file provided. From the main project folder in the terminal run:

```bash
createdb castingagency
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```

Note: You  may be required to delete the migrations folder before running the commands above.

## Running the server

Ensure that you are working using your created virtual environment.

From within the `casting-agency-api` directory, run the server by executing:

```bash
export FLASK_APP=wsgi
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `wsgi` directs flask to use the `backend` directory and the `app.py` file to find the application. 

## Endpoint Library

The endpoints can be tested on Postman to check on the corresponding returned objects for each endpoint.

Refer to the Postman collection file in the `casting-agency-api` folder.

### GET '/movies'

- General:
  - Fetches a dictionary of movies
  - Request Arguments: None
  - Returns: an object with keys movies and success. The movies key contains a list of id, title and release_date with their corresponding values.

- Sample:
```
{
  "movies": [
    {
      "id": 1,
      "release_date": "Feb 14, 2020",
      "title": "Sonic The Hedgehog"
    },
    {
      "id": 2,
      "release_date": "Feb 7, 2020",
      "title": "The Call Of the Wild"
    }
  ],
  "success": true
}

```

### GET '/actors'

- General:
  - Fetches a dictionary of actors
  - Request Arguments: None
  - Returns: an object with keys actors and success. The actors key contains a list of name, age, and gender with their corresponding values.

- Sample:
```
{
  "actors": [
    {
      "age": 58,
      "gender": "male",
      "id": 1,
      "name": "Jim Carrey"
    },
    {
      "age": 46,
      "gender": "male",
      "id": 2,
      "name": "James Marsden"
    }
  ],
  "success": true
}

```


## Testing

In order to carry out the tests on the endpoints, navigate to the backend folder in your terminal and run the following commands:

dropdb castingagency_test
createdb castingagency_test
psql castingagency_test < casting.psql
python3 test_flaskr.py


## License
The contents of this repository are covered under the MIT License.