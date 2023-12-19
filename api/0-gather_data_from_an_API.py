#!/usr/bin/python3
""" using this REST API """

import json
import requests
from sys import argv


API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':

    """ check user's informations """
    user_response = requests.get(f"{API_URL}/users/{argv[1]}")
    user_data = user_response.json()

    """ check user's to do list """
    to_do_response = requests.get(f"{API_URL}/todos?user_ID={argv[1]}")
    to_do_data = to_do_response.json()

    """ filter for task completed """
    completed_task = [task for task in to_do_data if task['completed']]

    """ display progression """
    employee_name = user_data["name"]
    num_task_completed = len(completed_task)
    total_task = len(to_do_data)
    print("Employee {} is done with task({}/{}):".format(
        employee_name, num_task_completed, total_task))

    for task in completed_task:
        print(f"\t {task['title']}")
