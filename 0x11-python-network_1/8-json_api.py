#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == '__main__':
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    param = {'q': letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=param)
    try:
        result = response.json()
        if result != {}:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
        else:
            print('No result')
    except ValueError as e:
        print('Not a valid JSON')
