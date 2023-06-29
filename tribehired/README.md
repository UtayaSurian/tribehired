# Technical Test #

This is a simple test that created using Django Rest Framework (DRF) concept.
There are two endpoints to handle Question 1 and Question 2 set by the tester from TribeHired.
Those two endpoints usage described as follows:


## Endpoints 
To start the endpoint services, user must start the Django server by running "python manage.py runserver" script from where the manage.py server script located.
Once started the server, user can now begin to test for both endpoints.
User can use any api testing tool like Postman to send request into endpoints.

### Enpoint for Question 1: http://localhost:8000/api/top_posts/
For this endpoint, user need to use 'GET' method to send api request using this above URL to return a list of Top Posts ordered by their number of comments.

### Endpoint for Question 2: http://localhost:8000/api/search/

For this endpoint, user need to use 'POST' method to send search api request by using the above URL.
This endpoint have few params set to be optional:
#### Param1: name
#### Param2: email
#### Param3: body
