 ## API 

- API that returns the PAN data, when given the PAN number as input. The API is made using [Flask Restex](https://flask-restx.readthedocs.io/en/latest/quickstart.html)

###  Runing the API 

- Clone the repository 

```bash
$ git clone https://github.com/Pratik-sys/API
```

- Navigate to  the clone repository 
```bash
$ cd API
```
- Run the app 

```bash
$ python3 app.py
```

- with the aabove instruction the flask server will start up 

### Fetching the PAN data 

> We can see this in action using CURL

- Generate the token for accesing the PAN data 

```bash
$ curl -H "Content-Type: application/json" -X POST \
  -d '{"username":"Dinesh Kumar","password":"test"}' http://localhost:8080/login
```

#### output 

```bash
  {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDc2OTIwMjEsIm5iZiI6MTYwNzY5MjAyMSwianRpIjoiYWQ3OTEyNDgtNWIwMi00NWQ3LWI3YTItZGE1NDk0MjZmNTY1IiwiZXhwIjoxNjA3NjkyOTIxLCJpZGVudGl0eSI6IkRpbmVzaCBLdW1hciIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.ehkwJB4lWM9_ZbIwC9chXDJ1qqgMjCx46A9fVpLAmWo"
  }

```
- After generating token save the token in to the variable


```bash
$ export TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDc2OTIwMjEsIm5iZiI6MTYwNzY5MjAyMSwianRpIjoiYWQ3OTEyNDgtNWIwMi00NWQ3LWI3YTItZGE1NDk0MjZmNTY1IiwiZXhwIjoxNjA3NjkyOTIxLCJpZGVudGl0eSI6IkRpbmVzaCBLdW1hciIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.ehkwJB4lWM9_ZbIwC9chXDJ1qqgMjCx46A9fVpLAmWo"
```

- Now the PAN data can be access with the help of generated token and the PAN nuber. 


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