#!/usr/bin/python3
"""
Python script to export data in the JSON format.

Requirements:
    Records all tasks from all employees
    Format must be:
    { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS},...]}
    File name must be: todo_all_employees.json
"""
import json
import requests

if __name__ == '__main__':
    filename = "todo_all_employees.json"
    req = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    req_id = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    with open(filename, "w") as f:
        d = {j.get("id"): [{'task': i.get('title'),
                            'completed': i.get('completed'),
                            'username': j.get('username')} for i in req
                           if j.get("id") == i.get('userId')]
             for j in req_id}
        json.dump(d, f)
