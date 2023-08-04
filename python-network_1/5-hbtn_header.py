#!/usr/bin/python3
"""__summary__
- Write a Python script that takes in a URL,
- sends a request to the URL and displays the value of the
- variable X-Request-Id in the response header
"""
import sys
import requests

if __name__ == '__main__':
    reqs = requests.get(sys.argv[1])
    print(reqs.headers.get("X-Request-Id"))
