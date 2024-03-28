#!/usr/bin/python3
"""a Python script that takes in a URL sends a request
to the URL and displays the body of the response
"""

import requests
import requests.exceptions
import sys


if __name__ == "__main__":

    if (len(sys.argv) != 2):
        q = ""
    else:
        q = sys.argv[1]

    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        js = req.json()
        if js == {}:
            print("No result")
        else:
            print(f"[{js.get('id')}] {js.get('name')}")
    except Exception:
        print("Not a valid JSON")
