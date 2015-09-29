__author__ = 'wm'


import requests
import json


def main():
    url = "http://192.168.58.129:80/wpd"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "echo",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers)

    print response

    response = response.json()

    assert response["result"] == "echome!"
    assert response["jsonrpc"]
    assert response["id"] == 0

    print response

if __name__ == "__main__":
    main()