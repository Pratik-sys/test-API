 ## API 

- API that returns the PAN data, when given the PAN number as input. The API is made using [Flask Restex](https://flask-restx.readthedocs.io/en/latest/quickstart.html) and [MongoEngine](http://docs.mongoengine.org/tutorial.html) for storing the user PAN details. The [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage/) for managing the authentication using JWT Bearer tokens.

###  Runing the API 

- Clone the repository 

```bash
$ git clone https://github.com/Pratik-sys/API
```

- Navigate to  the cloned repository 

```bash
$ cd API
```

- Run the app 

```bash
$ python3 app.py
```

- With the above instructions the flask server will starting runing on ```localhost:8080``` 

### Fetching the PAN details

> We can see this in action using ```CURL``` command

- Generate the token with the usernam and password for accesing the PAN data 

```bash
$ curl -H "Content-Type: application/json" -X POST \
  -d '{"username":"Dinesh Kumar","password":"test"}' http://localhost:8080/login
```

#### Output 

```bash
  {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDc2OTIwMjEsIm5iZiI6MTYwNzY5MjAyMSwianRpIjoiYWQ3OTEyNDgtNWIwMi00NWQ3LWI3YTItZGE1NDk0MjZmNTY1IiwiZXhwIjoxNjA3NjkyOTIxLCJpZGVudGl0eSI6IkRpbmVzaCBLdW1hciIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.ehkwJB4lWM9_ZbIwC9chXDJ1qqgMjCx46A9fVpLAmWo"
  }

```
- After generating token, save the token into the variable


```bash
$ export TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDc2OTIwMjEsIm5iZiI6MTYwNzY5MjAyMSwianRpIjoiYWQ3OTEyNDgtNWIwMi00NWQ3LWI3YTItZGE1NDk0MjZmNTY1IiwiZXhwIjoxNjA3NjkyOTIxLCJpZGVudGl0eSI6IkRpbmVzaCBLdW1hciIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.ehkwJB4lWM9_ZbIwC9chXDJ1qqgMjCx46A9fVpLAmWo"
```

- Now the PAN data can be accessed with the help of token and the PAN number as input. 


```bash 
$ curl -H "Authorization: Bearer $TOKEN" http://localhost:8080/ANRPM2537J
```

#### Output

```bash 
  {
    "client_id": "4feb601e-2316-4dda-8d91-28c89cdb2335",
    "dob": "Thu, 25 Oct 1990 00:00:00 GMT",
    "father_name": "Hari Kumar",
    "name": "Dinesh Kumar",
    "pan": "ANRPM2537J"
  }
```