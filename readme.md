# Soccer Manager Game API.

This project implements a backend to perform all operations needed for a simple application where football/soccer fans will create fantasy teams and will be able to sell and/or buy players.

# Getting Started.

## Pre-requisites and Local Environment.

### 1. Access the project files

The first step to use this API locally is download the project from GitLab using the following link: [project](https://git.toptal.com/screening/Rodrigo-Bernardo-Medeiros/-/tree/main/). There, choose the download button with the option "Download source code", choose the best extension file for you. After this, unzip the project and navigate until the directory `soccer-manager` (the first occurence), there we'll perform all operations and configurations. All following steps will be done inside this directory.

### 2. Python, Virtual Environment and requirements.

It's necessary to have python 3 and pip installed. The version used was `3.8.10 64 bits` and it is highly recommended to create a virtual environment in order to have an isolated development environment. All required packages are included in the requirements.txt file and before install it, let's first create a virtual environment to guarantee that all libraries are in the correct version. To create a virtual environment, open a terminal window in the directory `soccer-manager` and run the following command:

```
python -m venv env
```

Activate the virtual environment with the following command:

```
env\scripts\activate
```

Install all requirements with the following command:

```
pip install -r requirements.txt
```

### 3. Environment Variables

As best practice, it's common to use environment variables to keep configurations safe. For this project, it's necessary to define two environment variables, `SECRET_KEY` and `DEGUB`. These variables are used into django configurations, framework used to build this API.

- SECRET_KEY: encrypted value created when a django project is started
- DEBUG: Boolean that define the environment as `Development` or `Production`

First step is change the name of the file `.env_default` to just `.env`. Inside this file, set values for `SECRET_KEY` and `DEBUG`. For `SECRET_KEY` define any string and for `DEBUG` define as TRUE.

### 4. Create the database

To run this project locally, a database is needed to store all information. `SQLITE3` was a simple database that is used as default in django projects. For practicity, a `SQLITE3` database will be created for this API.
To create it just run the following command in the terminal:

```
python manage.py migrate
```

This command will create all tables and stabilish all relationships needed to manipulate information for this API.

# API Reference

Now that the environment is correctly configurated, the first step to use tand test this API is run the application locally, to do that, run the following command into terminal (remember to be inside the right directory with the python virtual environment activated).

```
python manage.py runserver
```

This command starts the application that can be running now using any browser directly with the following url http://127.0.0.1:8000/ (localhost - by default). With the application running we can explore each one of the endpoints.

- Base URL: http://127.0.0.1:8000/

This API was built in python using django and django rest frameworks. With this we have access to an administration panel where we can observe all created entries and an API interface where we can do tests for each endpoint.

## Endpoints

### POST /auth/register/

- General:
    - This endpoint is used to register new users, it's needed once only authenticated users can access the other endpoints.
    - This endpoint specifically don't have restrictions in access because it'is the entry point to the application.

__request:__

```json
{
    "username": "rodrigo",
    "password": "draGao01",
    "password2": "draGao01",
    "pmail": "rodrimedeiros@teste.com",
    "first_name": "rodrigo",
    "last_name": "bernardo medeiros"
}
```

__response:__

```json
{
    "username": "rodrigo",
    "email": "rodrimedeiros@teste.com",
    "first_name": "rodrigo",
    "last_name": "bernardo medeiros"
}
```

This endpoint creates a new user and the team with all players to start to play the game. There's only one team per player considering the email as the unique key.

### POST /auth/login/

- General:
    - Endpoint used to login into the application and let the user access other endpoints that needs authentication.

__request:__

```json
{
    "username": "rodrigo",
    "password": "draGao01",
}
```

__response:__

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NjY0ODIzMSwiaWF0IjoxNjU2NTYxODMxLCJqdGkiOiJiMzljNjEzMzdlMzg0ZTgxODIwNmUzMzRlZTAwMDRjYiIsInVzZXJfaWQiOjQsInVzZXJuYW1lIjoicm9kcmlnYW8ifQ.RdfPWSOa-6N6T2QLccuc1lBbQuVpgftvIKX_Jvhj85o",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU2NTYyMTMxLCJpYXQiOjE2NTY1NjE4MzEsImp0aSI6ImJiYWE4OTg4ZTRlYzRiYjM4OGFlOGI0YWYxMjBlYzM4IiwidXNlcl9pZCI6NCwidXNlcm5hbWUiOiJyb2RyaWdhbyJ9.8TlBAWsqmpuozdRx2vd8RUEiQCFAzID6PodEmfAY_WQ"
}
```

This endpoint let users login into API when credentials were passed correectly. As response we have tokens that can be used to access the API programatically or used to keep a session running into web browsers.

### POST /auth/login/refresh/

- General:
    - Endpoint used to refresh tokens when needed to keep the sessions running allowing continuous access.

__request:__

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NjY0ODIzMSwiaWF0IjoxNjU2NTYxODMxLCJqdGkiOiJiMzljNjEzMzdlMzg0ZTgxODIwNmUzMzRlZTAwMDRjYiIsInVzZXJfaWQiOjQsInVzZXJuYW1lIjoicm9kcmlnYW8ifQ.RdfPWSOa-6N6T2QLccuc1lBbQuVpgftvIKX_Jvhj85o"
}
```

__response:__

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU2NTYyOTE1LCJpYXQiOjE2NTY1NjE4MzEsImp0aSI6Ijk5Y2UyMDZlMGJlODQ0NDU4NDZjMmM0YjZjZjQ1ZDU1IiwidXNlcl9pZCI6NCwidXNlcm5hbWUiOiJyb2RyaWdhbyJ9.CKCBDEsR2t9BvAs72aW8t3I6EMrJnR0z_MdtmlSys3A"
}
```

Use this endpoint to get a refreshed token.

### GET /team/

- General:
    - Brings back team main information. This endpoint works only for authenticated users.


__response:__

```json
{
    "id": 10,
    "name": "Manchester City",
    "country": "Brazil",
    "team_value": 21750000.0,
    "budget": 3800000.0,
    "user": "renata"
}
```

### GET /players/

- General:
    - Brings back a list containing information of all players of the team. This endpoint works only for authenticated users.

__response:__

```json
[
    {
        "id": 122,
        "first_name": "first name_1",
        "last_name": "last name_1",
        "country": "United States",
        "age": 19,
        "position": "goalkeeper",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 123,
        "first_name": "first name_2",
        "last_name": "last name_2",
        "country": "United States",
        "age": 29,
        "position": "goalkeeper",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 124,
        "first_name": "first name_3",
        "last_name": "last name_3",
        "country": "United States",
        "age": 24,
        "position": "goalkeeper",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 125,
        "first_name": "first name_4",
        "last_name": "last name_4",
        "country": "United States",
        "age": 22,
        "position": "defender",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 126,
        "first_name": "first name_5",
        "last_name": "last name_5",
        "country": "United States",
        "age": 32,
        "position": "defender",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 127,
        "first_name": "first name_6",
        "last_name": "last name_6",
        "country": "United States",
        "age": 23,
        "position": "defender",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 128,
        "first_name": "first name_7",
        "last_name": "last name_7",
        "country": "United States",
        "age": 23,
        "position": "defender",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 129,
        "first_name": "first name_8",
        "last_name": "last name_8",
        "country": "United States",
        "age": 28,
        "position": "defender",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 130,
        "first_name": "first name_9",
        "last_name": "last name_9",
        "country": "United States",
        "age": 31,
        "position": "defender",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 131,
        "first_name": "first name_10",
        "last_name": "last name_10",
        "country": "United States",
        "age": 27,
        "position": "midfielder",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 132,
        "first_name": "first name_11",
        "last_name": "last name_11",
        "country": "United States",
        "age": 20,
        "position": "midfielder",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 133,
        "first_name": "first name_12",
        "last_name": "last name_12",
        "country": "United States",
        "age": 21,
        "position": "midfielder",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 134,
        "first_name": "first name_13",
        "last_name": "last name_13",
        "country": "United States",
        "age": 29,
        "position": "midfielder",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 135,
        "first_name": "first name_14",
        "last_name": "last name_14",
        "country": "United States",
        "age": 25,
        "position": "midfielder",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 136,
        "first_name": "first name_15",
        "last_name": "last name_15",
        "country": "United States",
        "age": 35,
        "position": "midfielder",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 137,
        "first_name": "first name_16",
        "last_name": "last name_16",
        "country": "United States",
        "age": 19,
        "position": "attacker",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 138,
        "first_name": "first name_17",
        "last_name": "last name_17",
        "country": "United States",
        "age": 22,
        "position": "attacker",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 139,
        "first_name": "first name_18",
        "last_name": "last name_18",
        "country": "United States",
        "age": 30,
        "position": "attacker",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 140,
        "first_name": "first name_19",
        "last_name": "last name_19",
        "country": "United States",
        "age": 20,
        "position": "attacker",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 141,
        "first_name": "first name_20",
        "last_name": "last name_20",
        "country": "United States",
        "age": 36,
        "position": "attacker",
        "value": 1000000.0,
        "team": "Manchester City"
    },
    {
        "id": 143,
        "first_name": "Gabi",
        "last_name": "Gol",
        "country": "Brazil",
        "age": 29,
        "position": "goalkeeper",
        "value": 1750000.0,
        "team": "Manchester City"
    }
]
```

This response is an example of an initial team containing 20 players.

### GET /players/< int:pk >/

- General:
    - Get information for a specific player based on the id. This endpoint is restricted for authenticated and only work for the owner of the specific player. If an user tries to access a players from other user, an exception is raised.

__response:__

```json
{
    "id": 122,
    "first_name": "first name_1",
    "last_name": "last name_1",
    "country": "United States",
    "age": 19,
    "position": "goalkeeper",
    "value": 1000000.0,
    "team": "Manchester City"
}
```

### PUT /players/< int:pk >/

- General:
    - Allow update of some fields of players: 
        - first_name
        - last_name
        - country
    - Same behavior of GET method regarding authenticated users and owners of the specific player.

__request:__

```json
{
    "first_name": "other first name",
    "last_name": "other last name",
    "country": "Brazil",
}
```

__response:__

```json
{
    "id": 122,
    "first_name": "other first name",
    "last_name": "other last name",
    "country": "Brazil",
    "age": 19,
    "position": "goalkeeper",
    "value": 1000000.0,
    "team": "Manchester City"
}
```

### PUT /team/< int:pk >/

- General:
    - Allow update of some fields of teams: 
        - name
        - country
    - Same behavior of players GET method regarding authenticated users and owners of the specific team.

__request:__

```json
{
    "name": "The Greatest Team",
    "country": "Brazil",
}
```

__response:__

```json
{
    "id": 10,
    "name": "The Greatest Team",
    "country": "Brazil",
    "team_value": 21750000.0,
    "budget": 3800000.0,
    "user": "renata"
}
```

### GET /transfer-market/

- General:
    - Get information of all players present on transfer market list.

``` json
[
    {
        "id": 122,
        "first_name": "other first name",
        "last_name": "other last name",
        "country": "Brazil",
        "age": 19,
        "position": "goalkeeper",
        "value": 1000000.0,
        "team": "The Greatest Team",
        "transfer_list": true,
        "transfer_value": 1200000.0
    },
    {
        "id": 123,
        "first_name": "first name_2",
        "last_name": "last name_2",
        "country": "United States",
        "age": 29,
        "position": "goalkeeper",
        "value": 1000000.0,
        "team": "The Greatest Team",
        "transfer_list": true,
        "transfer_value": 1200000.0
    },
    {
        "id": 161,
        "first_name": "first name_20",
        "last_name": "last name_20",
        "country": "United States",
        "age": 33,
        "position": "attacker",
        "value": 1000000.0,
        "team": "Manchester City",
        "transfer_list": true,
        "transfer_value": 800000.0
    }
]
```

### PUT /transfer-market/< int:pk >/add/

- General:
    - Include the player into the transfer market list.
    - As mentioned before the user only is allowed to transfer her own players to this list.

__request:__

```json
{
    "transfer_list": "true",
    "transfer_value": 750000,
}
```

__response:__

```json
{
    "id": 122,
    "first_name": "other first name",
    "last_name": "other last name",
    "country": "Brazil",
    "age": 19,
    "position": "goalkeeper",
    "value": 1000000.0,
    "team": "The Greatest Team",
    "transfer_list": true,
    "transfer_value": 750000.0
}
```

### PUT /transfer-market/< int:pk >/buy/

- General:
    - Buy one player from transfer market list.
    - Is responsible for update budgets, team values for both teams (buyer and seller) and player information.

__request:__

```json
No fields required for this endpoint
```

__response:__

```json
{
    "id": 122,
    "first_name": "other first name",
    "last_name": "other last name",
    "country": "Brazil",
    "age": 19,
    "position": "goalkeeper",
    "value": 1100000.0,
    "team": "Other team",
    "transfer_list": true,
    "transfer_value": 750000.0
}
```

# Tests

There are unit tests in two sections of this project, one to test register and authentication issues and another to test all endpoints correlated to teams and players.
These tests can be found into the following directories:

- `/auth/tests.py`
- `players_market/tests.py`

After adding pytest configuration file `pytest.ini`, it's possible to run all tests from the terminal with the following command (remember to be into soccer_manager directory):

'''
pytest
'''

This command collect all tests from all tests.py files in all parts from the project.

# Final Considerations

1. Using django rest framework user interface, it's possible to test all the endpoints.
2. Except /register/ endpoints, all others need authenticated users. 
3. Each user can make changes only on her team and players.

# Next Step

The next step would be to make the application available for use using docker or deploying it through Heroku or other platforms depending on the client's needs.