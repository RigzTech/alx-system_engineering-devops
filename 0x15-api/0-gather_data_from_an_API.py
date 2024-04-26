#!/usr/bin/python3
""" python script that, using this REST API,
 for a given employee ID """
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    r = requests.get(url)
    user = r.json()
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(user_id)
    r = requests.get(url)
    todos = r.json()
    done = []
    for todo in todos:
        if todo.get('completed') is True:
            done.append(todo)
    user_name = user.get('name')
    print('Employee {} is done with tasks({}/{}):'.format(user_name,
                                                          len(done),
                                                          len(todos)))
    for task in done:
        print('\t {}'.format(task.get('title')))
