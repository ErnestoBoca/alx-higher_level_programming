#!/usr/bin/python3
"""takes in a URL, sendthe URL and displays the value of the
variable X-Request-Id in the response header"""
import requests
import sys


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    if 'X-Request-Id' in response.headers.keys():
        print(response.headers['X-Request-Id'])
    else:
        print(None)
