# Casting Agency

The name of the application is called the Casting Agency.  The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. As an Executive Producer within the company, I am motivated in creating a system to simplify and streamline the processes.

## Deployment

This app is hosted on heroku. The link to the app is [here, click me!](https://stephangelcastingf.herokuapp.com). The backend is up and running. The frontend is still under construction. 

Refer to the credentials given below to login in order to access the JWT for each role mentioned below.  Ensure that your browser history is cleared at least for the last 1 hour before login into each account.

## Authentication
The app uses [Auth0](https://auth0.com) as a third party authentication service.

Three roles have been created to manage the system. Each role is restricted to perform certain CRUD operations on the system as assigned and permitted by Auth0 service.

The three roles are:

- Casting assistant 
  - Permission to `get:movies-details` and `get:actors-details`
  - Login info:
    - Email: `eaglecastassistant@gmail.com`
    - password: `Passwordeca1`

- Casting Director
  - All permissions a Casting Assistant has, as mentioned above.
  - Permission to `post:actors` and `delete:actors` 
  - Permission to `patch:actors` and `patch:movies`
  - Login info:
    - Email: `eaglecastdirector@gmail.com`
    - password: `Passwordecd1`

- Executive Producer
  - All permissions a Casting Director has, as mentioned above.
  - Permission to `post:movies` and `delete:movies` 
  - Login info:
    - Email: `eaglecastproducer@gmail.com`
    - password: `Passwordecp1`

## Getting Started with local development

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

## Running the server locally on your machine

Ensure that you are working using your created virtual environment.

In `backend/app.py` remove the `.` from line 7 and 8. 

Line 7 & 8 should look like this:
```
    from models import setup_db, Movie, Actor
    from auth import AuthError, requires_auth
```
### Issue#1
The `.` is required on line 7 and 8 when Heroku launches the app from the `wsgi.py` file found in the `casting-agency-folder`. The `.models` is equivalent to `backend.models`. It designates the path to the module. The issue is why the app can't be launched locally when the command lines below are executed in the terminal, unless the changes, as mentioned above, are made to lines 7 & 8.

From within the `casting-agency-api` directory, run the server by executing:

```bash
export FLASK_APP=wsgi
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect the changes made to the file and restart the server automatically.

Setting the `FLASK_APP` variable to `wsgi` directs flask to use the `backend` directory and the `app.py` file to find the application. 

## Endpoint Library

The endpoints can be tested on Postman to check on the corresponding returned objects for each endpoint.  

Refer to the Postman collection file in the `casting-agency-api` folder.  Remember to use the JWTs generated from the Auth0 login, refer to section Deployment and Authentication, in order to test the endpoints that required the necessary authentication and permission.

Alternatively, refer to the [postman docs](https://documenter.getpostman.com/preview/3439625-19dd2095-4442-4fc8-9127-2cf73f9dd824?versionTag=latest&apiName=CURRENT&version=latest&top-bar=ffffff&right-sidebar=303030&highlight=ef5b25#c1a80dc4-1465-43fc-bf7e-74327ab1102f) for this particular collection for the respective `Curl` commands for each endpoint. Remember to include the `headers={"Authorization": (ROLE's_JWT)}` at the end of each `curl` command where authorization is required for the endpoint.

### Endpoints for movies
#### GET '/movies'

- General:
  - Fetches a dictionary of movies
  - Request Arguments: The page_number. Default is set to page 1. The page number can be requested by adding `?page={page_number}` to the endpoint, e.g `/movies?page=2`.
  - Returns: an object with keys `movies` and `success`. The key `movies` contains a list of id, title and release_date with their corresponding values.

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

#### GET '/movies-details'

- General:
  - Fetches a dictionary of movies with full details
  - Request Arguments: The page_number. Default is set to page 1. The page number can be requested by adding `?page={page_number}` to the endpoint, e.g `/movies-details?page=2`.
  - Returns: an object with keys `movies `and `success`. The key `movies` is another object that contains a list of `actors`, the `id`, `release_date`, `title` of the movies. The list of actors provide the details of actors assigned to the movies.

- Sample:
```
    {
        "movies": [
            {
                "actors": [
                    {
                        "age": 58,
                        "gender": "male",
                        "id": 1,
                        "movie": 1,
                        "name": "Jim Carrey"
                    },
                    {
                        "age": 46,
                        "gender": "male",
                        "id": 2,
                        "movie": 1,
                        "name": "James Marsden"
                    }
                ],
                "id": 1,
                "release_date": "Feb 14, 2020",
                "title": "Sonic The Hedgehog"
            },
            {
                "actors": [
                    {
                        "age": 77,
                        "gender": "male",
                        "id": 3,
                        "movie": 2,
                        "name": "Harrison Ford"
                    },
                    {
                        "age": 42,
                        "gender": "male",
                        "id": 4,
                        "movie": 2,
                        "name": "Omar Sy"
                    },
                    {
                        "age": 32,
                        "gender": "female",
                        "id": 5,
                        "movie": 2,
                        "name": "Karen Gillan"
                    }
                ],
                "id": 2,
                "release_date": "Feb 7, 2020",
                "title": "The Call Of the Wild"
            }
        ],
        "success": true
    }
```

#### POST '/movies'

- General:
  - Add a movie with the required details. Only a registered Executive Producer have the permissions to add an actor.
  - Request Arguments: authentication token, an object containing the `title` and `release_date` of the new movie.
  - Returns: an object with keys `added_movie `and `success`. The key `added_movie` is another object that contains the `id`, `title` and `release_date` with their corresponding values. 

- Sample:
```
    {
        "added_movie": [
            {
                "id": 5,
                "release_date": "March 13, 2020",
                "title": "Bloodshot"
            }
        ],
        "success": true
    }
```
#### DELETE '/movies/{int:movie_id}'

- General:
  - Delete details of a movie. Only a registered Executive Producer have the permissions to delete an a movie.
  - Request Arguments: `movie.id`, authentication token
  - Returns: an object with keys `deleted_movie `and `success`. The key `deleted_movie` is another object that contains the `id`, `title` and `release_date` with their corresponding values. 

- Sample:
```
    {
        "deleted_movie": [
            {
                "id": 5,
                "release_date": "March 13, 2020",
                "title": "Bloodshot"
            }
        ],
        "success": true
    }
```
#### PATCH '/movies/{int:movie_id}'

- General:
  - update details about an movie. Only a registered Executive Producer have the permissions to update details about an actor.
  - Request Arguments: authentication token, `movie.id`, an object containing the keys `title` and `release_date` with the respective updated values.
  - Returns: an object with keys `updated_movie `and `success`. The key `updated_movie` is another object that contains the `id`, `title` and`release_date` with their corresponding updated values.

- Sample:
```
    {
        "success": true,
        "updated_movie": [
            [
                {
                    "id": 1,
                    "release_date": "June 27, 2020",
                    "title": "Sonic The Hedgehog"
                }
            ]
        ]
    }

```


### Endpoints for actors
#### GET '/actors'

- General:
  - Fetches a dictionary of actors
  - Request Arguments: The page_number. Default is set to page 1. The page number can be requested by adding `?page={page_number}` to the endpoint, e.g `/actors?page=2`.
  - Returns: an object with keys `actors` and `success`. The key `actors` contains a list of name, age, and gender with their corresponding values.

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

#### GET '/actors-details'

- General:
  - Fetches a dictionary of actors
  - Request Arguments:  The page_number. Default is set to page 1. The page number can be requested by adding `?page={page_number}` to the endpoint, e.g `/actors-details?page=2`.
  - Returns: an object with keys `actors` and `success`. The key `actors` contains a list of `id`, `name`, `age`, `gender` and `movie` with their corresponding values.

- Sample:
```
    {
        "actors": [
            {
                "age": 58,
                "gender": "male",
                "id": 1,
                "movie": 1,
                "name": "Jim Carrey"
            },
            {
                "age": 46,
                "gender": "male",
                "id": 2,
                "movie": 1,
                "name": "James Marsden"
            },
            {
                "age": 42,
                "gender": "male",
                "id": 4,
                "movie": 2,
                "name": "Omar Sy"
            },
            {
                "age": 32,
                "gender": "female",
                "id": 5,
                "movie": 2,
                "name": "Karen Gillan"
            },
            {
                "age": 37,
                "gender": "female",
                "id": 6,
                "movie": 3,
                "name": "Ali Wong"
            },
            {
                "age": 38,
                "gender": "female",
                "id": 7,
                "movie": 4,
                "name": "Andrea Riseborough"
            }
        ],
        "success": true
    }

```

#### DELETE '/actors/{int:actor_id}'

- General:
  - Delete details of an actor. Only a registered casting director and an executive Producer have the permissions to delete an actor.
  - Request Arguments: `actor.id`, authentication token
  - Returns: an object with keys `deleted_actor `and `success`. The key `deleted_actor` is another object that contains the `id`, `name`, `age` and `gender` with their corresponding values.

- Sample:
```
    {
        "deleted_actor": {
            "age": 77,
            "gender": "male",
            "id": 3,
            "name": "Harrison Ford"
        },
        "success": true
    }
```

#### POST '/actors'

- General:
  - Add an actor with the required details. Only a registered casting director and an executive Producer have the permissions to add an actor.
  - Request Arguments: authentication token, an object containing the `name`, `age`,`gender` and/or `movie` of the new actor.
  - Returns: an object with keys `added_actor `and `success`. The key `added_actor` is another object that contains the `id`, `name`, `age`, `gender` and `movie` with their corresponding values. The key `movie`, in this instance, is the assigned `movie_id` to this particular actor.

- Sample:
```
    {
        "added_actor": [
            {
                "age": 60,
                "gender": "Female",
                "id": 9,
                "movie": null,
                "name": "Margot Robbie"
            }
        ],
        "success": true
    }
```

#### PATCH '/actors/{int:actor_id}'

- General:
  - update details about an actor. Only a registered casting director and an executive Producer have the permissions to update details about an actor.
  - Request Arguments: `actor.id`, authentication token
  - Returns: an object with keys `updated_actor `and `success`. The key `updated_actor` is another object that contains the `id`, `name`, `age`, `gender` and `movie` with their corresponding values. The key `movie`, in this instance, is the assigned `movie_id` to this particular actor.

- Sample:
```
{
    "success": true,
    "updated_actor": [
        [
            {
                "age": 25,
                "gender": "Female",
                "id": 9,
                "movie": 2,
                "name": "Margot Robbie"
            }
        ]
    ]
}
```
## Testing

In order to carry out the tests on the endpoints, navigate to the backend folder in your terminal and run the following commands:

```bash
source setup.sh
dropdb castingagency_test
createdb castingagency_test
psql castingagency_test < casting.psql
python3 test_flaskr.py
```

## License
The contents of this repository are covered under the [MIT License.](https://choosealicense.com/licenses/mit/)