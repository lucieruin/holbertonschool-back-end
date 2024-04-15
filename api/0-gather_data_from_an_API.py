#!/usr/bin/python3
""" using REST API for specific user with ID for have TO DO list progress """

import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com/"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : ./0-gather_data_from_an_API.py <employee id>")
        sys.exit(1)

    id = sys.argv[1]

    """ check user informations """
    employee = requests.get(API_URL + "users/{}".format(id)).json()

    """ check user todolist """
    todo_list = requests.get("{}todos?userId={}".format(API_URL, id)).json()

    """ filter for task complete """
    complete_task = [task.get("title")
                     for task in todo_list if task.get("completed") is True]

    """ display progression """
    print("Employee {} is done with task({}/{}):".format(
        employee.get("name"), len(complete_task), len(todo_list)))

    for task in complete_task:
        print("\t {}".format(task))
