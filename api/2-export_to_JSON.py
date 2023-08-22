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
    index = int(sys.argv[1])

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_data = must(first(filter(users, 'id', index)),
                     ValueError("user not found"))
    user_todos = filter(todos, 'userId', user_data['id'])
    final = {}
    for v in user_todos:
        if v['userId'] not in final:
            final[v['userId']] = []

        final[v['userId']].append({
            'task': v['title'],
            'completed': v['completed'],
            'username': user_data['username'],
        })

    write_json('%s.json' % index, final)


if __name__ == '__main__':
    main()
