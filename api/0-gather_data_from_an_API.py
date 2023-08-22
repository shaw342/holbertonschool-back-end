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


def main():
    index = int(sys.argv[1])

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_data = must(first(filter(users, 'id', index)),
                     ValueError("user not found"))
    user_todos = filter(todos, 'userId', user_data['id'])
    user_todos_done = filter(user_todos, 'completed', True)
    user_todos_left = filter(user_todos, 'completed', False)

    print('Employee %s is done with tasks(%s/%s):' %
          (user_data['name'], len(user_todos_done), len(user_todos)))
    for v in user_todos_done:
        print('\t %s' % (v['title']))


if __name__ == '__main__':
    main()