#!/usr/bin/python3
""" api """
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


def main():
    index = int(sys.argv[1])

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_data = must(first(filter(users, 'id', index)),
                     ValueError("user not found"))
    user_todos = filter(todos, 'userId', user_data['id'])

    output = ''
    for todo_data in user_todos:
        final = [
            user_data['id'],
            user_data['username'],
            todo_data['completed'],
            todo_data['title'],
        ]
        final = ['"%s"' % str(v) for v in final]
        final = ','.join(final)
        output += final + '\n'

    write('%s.csv' % index, output)


if __name__ == '__main__':
    main()
