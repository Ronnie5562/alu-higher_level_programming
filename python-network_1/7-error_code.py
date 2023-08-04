#!/usr/bin/python3
"""__summary__
- Write a Python script that takes in a URL,
- sends a request to the URL and
- displays the body of the response.
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    reqs = requests.get(url)
    if reqs.status_code >= 400:
        print('Error code: {}'.format(reqs.status_code))
    else:
        print(reqs.text)
