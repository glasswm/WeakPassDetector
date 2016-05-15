# -*- coding: utf-8 -*-

from client.__setting__ import wp_server, proxies, reg_server, serial_key, TOP_N, STRONG, USER_CUSTOM, LENGTH_8_SPECIAL, \
    LENGTH_8_CHAR, LENGTH_8_NUM, LESS_THAN_8

__author__ = 'wm'


import requests
import json
import wx


def patch_crypto_be_discovery():

    """
    Monkey patches cryptography's backend detection.
    Objective: support pyinstaller freezing.
    """

    from cryptography.hazmat import backends

    try:
        from cryptography.hazmat.backends.commoncrypto.backend import backend as be_cc
    except ImportError:
        be_cc = None

    try:
        from cryptography.hazmat.backends.openssl.backend import backend as be_ossl
    except ImportError:
        be_ossl = None

    backends._available_backends_list = [
        be for be in (be_cc, be_ossl) if be is not None
    ]

patch_crypto_be_discovery()

from cryptography.fernet import Fernet
key = 'M3ZkzmsiNCJHoV57K3dG0r4-gtkhfdpYMAlRoIZg4Kg='
encrypt_obj = Fernet(key)

def weakt2str(wt):
    if wt == TOP_N:
        return 'TOP_N'
    elif wt == LESS_THAN_8:
        return u'长度小于8位'
    elif wt == LENGTH_8_NUM:
        return u'8位纯数字'
    elif wt == LENGTH_8_CHAR:
        return u'8位纯字母'
    elif wt == LENGTH_8_SPECIAL:
        return u'8位纯特殊字符'
    elif wt == USER_CUSTOM:
        return u'自定义字典'
    elif wt == STRONG:
        return u'健壮'
    else:
        return u'未知'

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
        url, data=encrypt_obj.encrypt(json.dumps(payload)), headers=headers)

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
    weak_type_list = []
    strong_list = []
    unknown_count = 0

    split_size = 10000

    for i in range(0, len(cipher_list), split_size):
        #print cipher_list[i:i+split_size]
        payload = {
            'method': 'check_weak_pass',
            'params': {'encrypt_algorithm' : encrypt_algorithm,
                       'cipher_list': cipher_list[i:i+split_size]},
            'jsonrpc': "2.0",
            'id': 0,
        }
        try:
            response = requests.post(url, data=encrypt_obj.encrypt(json.dumps(payload)), headers=headers) #, proxies=proxies)
            response = response.json()
            #print response
            res = response["result"]
            weak_list = weak_list + [kkk+i for kkk in res[0]]
            weak_type_list = weak_type_list + res[1]
            strong_list = strong_list + [kkk+i for kkk in res[2]]
            unknown_count = unknown_count + res[3]
        except Exception as e:
            print e.message
            dlg = wx.MessageDialog(None, u"无法连接到弱口令鉴定服务器", u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()

    for i in range(0, len(weak_type_list)):
        weak_type_list[i] = weakt2str(weak_type_list[i])

    return weak_list, strong_list, unknown_count, weak_type_list


def check_serial(serial_key):
    url = reg_server
    headers = {'content-type': 'application/json'}

    payload = {
        'method': 'verify',
        'params': {'serial_key' : serial_key},
        'jsonrpc': "2.0",
        'id': 0,
    }
    try:
        response = requests.post(url, data=encrypt_obj.encrypt(json.dumps(payload)), headers=headers, timeout=5) #, proxies=proxies)
        response = response.json()
        #print response
        res = response['result']
    except Exception as e:
        print e.message
        res = -2
    return res

# def add_log(message):
#     pass
def add_log(message):
    url = reg_server
    headers = {'content-type': 'application/json'}

    payload = {
        'method': 'addLog',
        'params': {'message': message},
        'jsonrpc': "2.0",
        'id': 0,
    }
    response = requests.post(url, data=encrypt_obj.encrypt(json.dumps(payload)), headers=headers) #, proxies=proxies)
    response = response.json()
    #print response



if __name__ == '__main__':
    #print check_weakpass('md5', ['c6cb4a50452a6f54c0e47612b974644c', 'd79c8788088c2193f0244d8f1f36d2db', 'c4ca4238a0b923820dcc509a6f75849b', '6c8349cc7260ae62e3b1396831a8398f', 'aab3238922bcc25a6f606eb525ffdc56', 'e10adc3949ba59abbe56e057f20f883e','81dc9bdb52d04dc20036dbd8313ed055','52c69e3a57331081823331c4e69d3f2e', '10fc61396e705b62a7df81b895611312'])
    #(7852424, 7777, 1, 45, 123456, 1234, 999999, 1234ab7c)
    #check_serial(serial_key)
    check_serial('1111')
    add_log(u'你好啊2222')
    #main()
