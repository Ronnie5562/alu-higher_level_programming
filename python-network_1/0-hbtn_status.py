#!/usr/bin/python3
"""__summary__
- Write a Python script that fetches https://alu-intranet.hbtn.io/status
- using the urllib package.
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alu-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
