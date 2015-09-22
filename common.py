__author__ = 'wm'

from enum import Enum

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


#DATABASE_ENUM = ('mysql', 'oracle')
#ENCRYPT_ALGORITHM_ENUM = ('md5', 'sha1')
