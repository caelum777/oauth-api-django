## Synopsis

This application uses django 2, django REST framework and the oauth toolkit to authenticate 
users. The application will return a valid token for users to pull data from API.


## Installation

Pre-requisites, install them according to your system:

* Pipenv
* Python 3.8


1. Clone the repository or create a fork 

2. Run pipenv

```shell
    pipenv install
```

3. Create a django superuser

```shell
    pipenv install
```

4. Create a django superuser

```shell
    python manage.py createsuperuser
```

5. Run migrations

```shell
    python manage.py migrate
```

6. Run server

```shell
    python manage.py runserver
```

7. Create oauth application (It has to be called **users**, **VERY IMPORTANT!**)
* First login with superuser at http://localhost:8000/admin
* Now go to http://localhost:8000/o/applications
* Click on New Application, it's a green button
* Name it **users**
* Client type **confidential**
* Authorization Grant Type **password**
* Redirect Uris **leave it blank**
* Click save

8. It's all done, just go to http://localhost:8000 and you should see a **login screen** and
you can register a new user clicking **No account? Register here**

## Endpoints

Register Endpoint:
```shell
    POST /authentication/register/ {"email": "email@domain.com", "password": "password"}
```

Token Endpoint:
```shell
    POST /authentication/token/ {"email": "email@domain.com", "password": "password"}
```

Revoke Token Endpoint:
```shell
    POST /authentication/token/ {"token": "<token>"}
```

Refresh Token Endpoint:
```shell
    POST /authentication/token/ {"refresh_token": "<token>"}
```

Basic User Info Endpoint:
```shell
    GET /authentication/session_details/ Authorization: Bearer <TOKEN>
```

## Possible improvements

* Allow just one token per user
* Generate "users" application programmatically
* Encrypt password on requests
* Manage exception messages on one place