#!/usr/bin/python3
"""a Python script that takes your GitHub credentials
and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    b = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get('https://api.github.com/user', auth=b)
    print(req.json().get("id"))
