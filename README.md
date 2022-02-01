# todo-app
Create an Api in python

1. Create a task
```Bash
curl -X POST -d '{"task_name": "task1"}' -H 'Content-Type: application/json' htt
p://localhost:5000/task
# HTTP status code - 201
# Output - empty

curl -X POST -d '{"task_name": "task1"}' -H 'Content-Type: application/json' htt
p://localhost:5000/task
# HTTP status code - 201
# Output - empty
```


2. View all tasks

```Bash
curl -X GET http://localhost:5000/task
# HTTP status code - 200
# Output
[
{
"id": 1,
"task_name": "task2",
"created_at": creation_timestamp_format_YYYY-MM-DD-HH-MM-SS,
"updated_at": updation_timestamp_format_YYYY-MM-DD-HH-MM-SS,
},
{
"id": 2,
"task_name": "task2",
"created_at": creation_timestamp,
"updated_at": updated_timestamp,
}
]
```

3. View a specific task
```Bash
curl -X GET http://localhost:5000/task/1
# HTTP status code - 200
# Output
{
"id": 1,
"task_name": "task2",
"created_date": creation_timestamp_format_YYYY-MM-DD-HH-MM-SS,
}

curl -X GET http://localhost:5000/task/22
# HTTP status code - 404
# Output
{
"error": "Invalid task id"
}
```



4. Update a specific task
```Bash
curl -X PUT -d '{"task_name": "task1 updated"}' -H 'Content-Type: application/jso
n' http://localhost:5000/task/1
# HTTP status code - 200
# Output
{
"id": 1,
"task_name": "task2",
"created_date": creation_timestamp_format_YYYY-MM-DD-HH-MM-SS,
}
```
5. Delete a specific task
```Bash
curl -X DELETE http://localhost:5000/task/1
# HTTP status code - 200
# Output - empty

curl -X DELETE http://localhost:5000/task/22
# HTTP status code - 404
# Output
{
"error": "Invalid task id"
}
```

Create a docker image and push the same to your local dockerhub, Use Github actions for creating a release and uploading the image.
