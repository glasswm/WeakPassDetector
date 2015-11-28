# -*- coding: utf-8 -*-
import  wx
import hashlib
import time
import datetime
import string

def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

# 逆序、md5
def crypt(str):
    sstr = str[::-1]
    return md5(sstr)

#return lasting time
def updateDtime(t):
    p = t.split('-')
    (a,b,c,d,e,f,g,h,i) = time.localtime(time.time())
    d1 = datetime.datetime(a,b,c)
    d2 = datetime.datetime(string.atoi(p[0]),string.atoi(p[1]),string.atoi(p[2]))
    return (d1-d2).days

def curTime():
    (a,b,c,d,e,f,g,h,i) = time.localtime(time.time())
    strTime = str(a) + '-' + str(b) + '-' + str(c)
    print strTime
    return strTime

if __name__ == '__main__':
    updateDtime('2015-1-5')
    curTime()
