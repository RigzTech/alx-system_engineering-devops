#!/usr/bin/python3
"""
script to export data in the CSV format,
and save it in a file named USER_ID.csv from a REST API
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}' \
        .format(user_id)
    r = requests.get(url)
    r_json = r.json()
    url = 'https://jsonplaceholder.typicode.com/users/{}' \
        .format(user_id)
    r = requests.get(url)
    r_json_user = r.json()
    user_name = r_json_user.get('username')

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in r_json:
            writer.writerow([
                user_id,
                user_name,
                task.get('completed'),
                task.get('title'),
            ])
    csvfile.close()
    print("File {}.csv created successfully".format(user_id))
