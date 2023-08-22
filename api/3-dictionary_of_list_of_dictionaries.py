#!/usr/bin/python3
""" api """
import json
import requests
import sys


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
        file.write(data)


def write_json(path, data):
    with open(path, 'w') as file:
        json.dump(data, file)


def main():
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    final = {}
    for user_data in users:
        user_todos = filter(todos, 'userId', user_data['id'])
        for v in user_todos:
            if v['userId'] not in final:
                final[v['userId']] = []

            final[v['userId']].append({
                'task': v['title'],
                'completed': v['completed'],
                'username': user_data['username'],
            })

        write_json('todo_all_employees.json', final)


if __name__ == '__main__':
    main()
