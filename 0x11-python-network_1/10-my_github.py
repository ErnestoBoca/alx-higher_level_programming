#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=basic).json()
    print(response.get('id'))
