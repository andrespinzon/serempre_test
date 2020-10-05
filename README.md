## TEST SEREMPRE

The service only received int values
```
http://www.dneonline.com/calculator.asmx?WSDL
```


### Run Project
First step: 
```
docker-compose up -d
```
Second step: 
```
docker-compose up
```

### URL's

##### ROOT: 
```
    http://localhost:8000/
```

##### ADMIN: 
```
    http://localhost:8000/admin
```

##### USER ADMIN:
```
    http://localhost:8000/admin
```
```
    username: serempre
    password: Serempre2020
```


### CURL 

#### Create task from API
```
curl --request POST \
  --url http://localhost:8000/api/tasks/ \
  --header 'content-type: application/json' \
  --cookie csrftoken=SNVznENXevOgrPPi4qTfdqNAFNlHMvOB1sLbwkxRWdKLsiYREfyIRaTpG5KP8eI9 \
  --data '{
	"developer": "Albert Einstein", 
	"title":"First Task in serempre",
	"description": "I am a robot",
	"time_worked": 1.5,
	"estimated_time": 5, 
	"is_completed": false
}'
```

Response: 

```
{
  "id": 1,
  "developer": "Albert Einstein",
  "title": "First Task in serempre",
  "description": "I am a robot",
  "time_worked": 1,
  "estimated_time": 5.0,
  "is_completed": false
}
```