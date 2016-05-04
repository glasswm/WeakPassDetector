__author__ = 'glasswm'

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('main.cfg')

LOCAL_DB_File = config.get('Crack', 'local_db')

# wp_server = 'http://192.168.238.132:4000/wpd'
wp_server = config.get('Crack', 'wp_server')
reg_server = config.get('Register', 'reg_server')

serial_key = config.get('Register', 'serial_key')

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}

# detect_period = 10
detect_period = config.get('Crack', 'detect_period')

account_limit = config.get('Crack', 'account_limit')

TOP_N = 0
LESS_THAN_8 = 1
LENGTH_8_NUM = 2
LENGTH_8_CHAR = 3
LENGTH_8_SPECIAL = 4
USER_CUSTOM = 5

STRONG = 9
