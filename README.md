# Instructions to run the code; 
You will need:
- Python 3.8 or above
- Docker

You can create a virtualenv and install the dependencies(requirements.txt) like our ancestors or:

```
$ docker-compose up --build -d
```

Now you got the server to run POST requests on 
```
http://0.0.0.0:8000/generate-risk-score/ 
```
with the pattern:
```
{
  "age": 35,
  "dependents": 2,
  "house": {"ownership_status": "owned"},
  "income": 0,
  "marital_status": "married",
  "risk_questions": [0, 1, 0],
  "vehicle": {"year": 2018}
}
```
P.S: Use a tool like Postman to test the API because when you up the server with -d theres no stdout in terminal.

Run the tests using:
```
$ docker exec -it useorigin bash
$ pytest .
```

To exit the container bash terminal:
```
$ exit
```

To see thee docs, just access: 
```
http://localhost:8000/docs
```

# What were the main technical decisions you made; 
1. Tech Stack: As I had the privilege of choosing the stack, I decided to use fastapi because it is one of the technologies that I have least worked on and has greater relevance nowadays for its simplicity, for allowing async and also automatically generating documentation. I believe that in a selection process, dealing with never-before-seen challenges presents our creative capacity better and not just memory. Continuous learning is my goal and therefore routine.
2. Architecture: Choose MVC architecture because it is the most common one and it is easy to understand. We can easily understand the architecture and the code with high coesion, low coupling and ease modification.

3. Tests: tested: Verify correct HTTP status code, Verify response payload. Checking valid JSON body and correct field names, types, and values — including in error responses and Verify response headers. 

# Relevant comments about your project
Improvements:
- Insert a STRATEGY design pattern to remove if conditions in risk_managment.py
- Insert oauth2 authentication to remove hardcoded credentials
- Insert a database to store the data