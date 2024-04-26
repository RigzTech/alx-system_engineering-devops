#!/usr/bin/python3
"""
Records all tasks that are owned by this employee from API to json
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_req = requests.get(user_url)
    user_json = user_req.json()
    username = user_json.get('username')
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user_id)
    todo_req = requests.get(todo_url)
    todo_json = todo_req.json()
    todo_dict = {}
    todo_list = []
    for task in todo_json:
        todo_dict = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        }
        todo_list.append(todo_dict)
    json_dict = {user_id: todo_list}
    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump(json_dict, json_file)
