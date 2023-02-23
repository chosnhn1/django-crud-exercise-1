# Sample Django based RESTful CRUD App

HOW TO

* Start your Python virtual environment and set it with `requirements.txt`
* Start application with `python manage.py runserver`

Requests:

* Log in via `api/token/`
* GET `articles/` to get article lists. POST articles with Bearer access token.
* GET, PATCH and DELETE to `articles/<int:pk>`.