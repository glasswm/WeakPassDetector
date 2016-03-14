__author__ = 'glasswm'


import ConfigParser


config = ConfigParser.RawConfigParser()
config.read('main.cfg')

LOCAL_DB_File = config.get('Crack', 'local_db')

#wp_server = 'http://192.168.238.132:4000/wpd'
wp_server = config.get('Crack', 'wp_server')

proxies = {
  "http": "http://127.0.0.1:8080",
  "https": "http://127.0.0.1:8080",
}

#detect_period = 10
detect_period = config.get('Crack', 'detect_period')