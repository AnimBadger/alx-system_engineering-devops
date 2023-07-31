#!/usr/bin/python3
''' retrieve information from API endpoint'''
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    completed = [_.get('title') for _ in todos if _.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.
          format(user.get('name'), len(completed), len(todos)))
    [print('\t {}'.format(_)) for _ in completed]
