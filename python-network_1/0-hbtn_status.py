#!/usr/bin/python3
"""__summary__
- Write a Python script that fetches https://alu-intranet.hbtn.io/status
- using the urllib package.
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as reqs:
        data = reqs.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
