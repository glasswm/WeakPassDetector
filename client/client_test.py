from client.__setting__ import wp_server, proxies

__author__ = 'wm'


import requests
import json


def main():
    url = wp_server
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "foobar",
        "params": {'foo' : "ni", 'bar': 'hao'},
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers)

    print response

    response = response.json()

    assert response["result"] == "nihao"
    assert response["jsonrpc"]
    assert response["id"] == 0

    print response


def check_weakpass(encrypt_algorithm, cipher_list):
    url = wp_server
    headers = {'content-type': 'application/json'}

    weak_list = []
    strong_list = []
    unknown_count = 0

    split_size = 1000

    for i in range(0, len(cipher_list), split_size):
        print cipher_list[i:i+split_size]
        payload = {
            'method': 'check_weak_pass',
            'params': {'encrypt_algorithm' : encrypt_algorithm,
                       'cipher_list': cipher_list[i:i+split_size]},
            'jsonrpc': "2.0",
            'id': 0,
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers) #, proxies=proxies)
        response = response.json()
        #print response
        res = response["result"]
        weak_list = weak_list + [kkk+i for kkk in res[0]]
        strong_list = strong_list + [kkk+i for kkk in res[1]]
        unknown_count = unknown_count + res[2]
        print response

    return weak_list, strong_list, unknown_count

if __name__ == '__main__':
    print check_weakpass('md5', ['c6cb4a50452a6f54c0e47612b974644c', 'd79c8788088c2193f0244d8f1f36d2db', 'c4ca4238a0b923820dcc509a6f75849b', '6c8349cc7260ae62e3b1396831a8398f', 'aab3238922bcc25a6f606eb525ffdc56', 'e10adc3949ba59abbe56e057f20f883e','81dc9bdb52d04dc20036dbd8313ed055','52c69e3a57331081823331c4e69d3f2e', '10fc61396e705b62a7df81b895611312'])
    #(7852424, 7777, 1, 45, 123456, 1234, 999999, 1234ab7c)
    #main()
