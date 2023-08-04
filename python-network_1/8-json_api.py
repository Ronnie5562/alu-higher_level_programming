#!/usr/bin/python3
"""__summary__
- Write a Python script that takes in a letter
-  and sends a POST request to http://0.0.0.0:5000/search_user 
- with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if (sys.argv[1]) else ""
    value = {"q": letter}

    reqs = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        data = reqs.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
