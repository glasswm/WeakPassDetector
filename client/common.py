# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.shortcuts import render

import django

import time
from django.template.defaultfilters import join

__author__ = 'wm'

from enum import Enum

db_type_list = ['mysql', 'oracle']
crypt_type_list = ['md5', 'sha1']

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

class DatabaseType(Enum):
    mysql = 'mysql'
    oracle = 'oracle'
    sqlserver = 'sqlserver'
    sqlite = 'sqlite'

class EncryptAlgorithmType(Enum):
    md5 = 'md5'
    sha1 = 'sha1'
    sha256 = 'sha256'
    plaintext = 'plaintext'


def generate_statement(sys_name, operator, time, weak_list, total_count, unkown_count):

    # res = render(None, 'report.html', {'sys_name':sys_name,
    #                                 'operator': operator,
    #                                 'time': time,
    #                                 'total_count': total_count,
    #                                 'unkown_count': unkown_count,
    #                                 'weak_list': weak_list})

    weaklist_str = ''

    for count, i in enumerate(weak_list):
        weaklist_str += '''
        <tr>
            <td>''' + str(count+1) + '''</td>
            <td>''' + i["name"] + '''</td>
            <td>''' + i["wtype"] + '''</td>
        </tr>
        '''

    res = open(os.path.dirname(__file__) + '/report/report.html', 'r').read().decode("utf-8")

    print res
    res = res.replace("{{ sys_name }}", sys_name);
    res = res.replace("{{ operator }}", operator);
    res = res.replace("{{ time }}", time);
    res = res.replace("{{ total_count }}", str(total_count));
    res = res.replace("{{ weak_count }}", str(len(weak_list)));
    res = res.replace("{{ weaklist }}", weaklist_str);

    out = open(os.path.dirname(__file__) + '/report/report'+ time +'.html', 'w')
    out.write(res.encode('utf-8'))
    out.close()


#DATABASE_ENUM = ('mysql', 'oracle')
#ENCRYPT_ALGORITHM_ENUM = ('md5', 'sha1')

if __name__ == '__main__':
    settings.configure()
    TEMPLATE_DIRS = (
        os.path.join(os.path.dirname(__file__), 'report').replace('\\','/'),
    )
    print TEMPLATE_DIRS
    django.setup()
    weak_list = [{'name' : 'aaaa1', 'wtype' : '1'},
                 {'name' : 'aaaa2', 'wtype' : '2'},
                 {'name' : 'aaaa3', 'wtype' : '1'},
                 {'name' : 'aaaa4', 'wtype' : '3'},
                 {'name' : 'aaaa5', 'wtype' : '1'},]
    generate_statement(u'基建管理信息系统', u'汪明', time.strftime('%Y-%m-%d',time.localtime(time.time())), weak_list, 14321, 111)