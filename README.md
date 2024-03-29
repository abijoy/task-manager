# Task Manager Application

## How to run the project
### Clone the repository
`https://github.com/abijoy/task-manager.git`

`cd task-manager`

## Run the project using Docker

create env files: `.env` and `.env.db` and make necessary changes according to `.env.example` and `.env.db.example`

after you are done with creating the env files, run:

`docker-compose build`

`docker-compose up`

Note: make sure you have docker installed on your system.

## Or run the project ususal way
### Install the required packages

First create and activate virtual environment then install the required packages.

`python3 -m venv .venv`

`source .venv/bin/activate`

`pip install -r requirements.txt`

### Configure your PostgreSQL database
If you are using Linux please refer to this blog post to install and configure PostgreSQL

**https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04**



### Set up the .env file
`cat .env.example > .env`

In your `.env` set the following environment variables:

DJANGO SPECIFIC CONFIG
* `SECRET_KEY`: add a arbitrary secret key needed by django
* `DEBUG`: set either `True` or `False`

DATABASE CONFIG
* `DB_NAME`:  set your postgreSQL database name.
* `DB_USER`: set your database username.
* `DB_PASSWORD`: set your database user password.

EMAIL CONFIG
* `EMAIL_HOST`: Your email host(i.e. smtp.gmail.com ) 
* `EMAIL_PORT`: 587
* `EMAIL_HOST_USER`: Your email address.
* `EMAIL_HOST_PASSWORD`: Your email password.

Carefully modify your  `.env` file.

### Now perform database migration
`python manage.py migrate`

### Now load the sample JSON fixtures
`python manage.py loaddata sample_data.json`


## Run the server
`python manage.py runserver`

the application will be running on **http://127.0.0.1:8000/**

### Sample Users credentials to interact with the system

`username:alamin` `password:1234`

`username:abijoy` `password:1234`

`username:spike` `password:1234`

### Create superuser to access admin panel

`python manage.py createsuperuser`

## API Endpoints

### List All The Tasks

Endpoint: `GET /api/v1/`

Simple Response:
```json
[
    {
        "id": 1,
        "title": "Finish project proposal",
        "description": "Complete the final draft of the project proposal and submit it to the client.",
        "due_date": "2023-12-30",
        "priority": "HIGH",
        "is_completed": false
    },
    {
        "id": 4,
        "title": "Complete bug fixes",
        "description": "Address the reported bugs in the software application.",
        "due_date": "2024-01-30",
        "priority": "LOW",
        "is_completed": false
    }
]
```
### Retrieve A Task

Endpoint: `GET /api/v1/{pk}/`

Example: `GET /api/v1/1/`

Response:
```json
{
    "id": 1,
    "title": "Finish project proposal",
    "description": "Complete the final draft of the project proposal and submit it to the client.",
    "due_date": "2023-12-30",
    "priority": "HIGH",
    "is_completed": false
}
```
### Create A New Task

Endpoint: `POST /api/v1/`

Request Body: 
```json
{
    "title": "Creating Task from API",
    "description": "This Task is creating from the API for Testing",
    "due_date": "2024-12-30",
    "priority": "MEDIUM",
    "is_completed": false
}
```
Response:

id is created automatically after saving the task.
```json
{
    "id": 11,
    "title": "Creating Task from API",
    "description": "This Task is creating from the API for Testing",
    "due_date": "2024-12-30",
    "priority": "MEDIUM",
    "is_completed": false
}
```
### Update A Task
  Endpoint: `PUT /api/v1/{pk}/`

  Endpoint: `PATCH /api/v1/{pk}/`

  Sample Request using `PATCH` Method:

  Example: `PATCH /api/v1/11/`

  Request body
  ```json
  {
      "title": "Creating Task from API(UPDATED)"
  }
  ```
  Response: 
  ```json
  {
    "id": 11,
    "title": "Creating Task from API(UPDATED)",
    "description": "This Task is creating from the API for Testing",
    "due_date": "2024-12-30",
    "priority": "MEDIUM",
    "is_completed": false
  }
  ```

  
### Delete A Task
  Endpoint: `DELETE /api/v1/{pk}`
  
  Example: `DELETE /api/v1/11/`
  
  Status: 204 No content. The server successfully deleted the resource.

