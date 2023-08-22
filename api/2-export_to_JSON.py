#!/usr/bin/python3
""" api """
import requests
import sys
import json


def filter(data, key, val):
    return [v for v in data if v[key] is val]


def first(data):
    if len(data) < 1:
        return None

    return data[0]


def must(value, error):
    if value is None:
        raise error

    return value


def write(path, data):
    with open(path, 'w') as file:
        json.dump(data, file)


def main():
    index = int(sys.argv[1])

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_data = must(first(filter(users, 'id', index)),
                     ValueError("user not found"))
    user_todos = filter(todos, 'userId', user_data['id'])
    final = {}
    for todo_data in user_todos:
        if todo_data["userId"] not in final:
            final[todo_data["userId"]] = []
            
        final[todo_data["userId"]].append({
                "task": todo_data["title"],
                "completed": todo_data["completed"],
                "username": user_data["username"]
            })
    write('%s.csv' % index, final)


if __name__ == '__main__':
    main()
