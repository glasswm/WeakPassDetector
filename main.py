__author__ = 'wm'

from common import DatabaseType, EncryptAlgorithmType
from models import SystemInfo, DBUtil


def test():
    db_util = DBUtil()
    id = 12
    print '____________________%d' % id
    s =  db_util.get_system_by_id(id)
    print s
    s.get_account_data(username='root', password='7410')


def demotest():
    db_util = DBUtil()

    #create
    demo_system = SystemInfo(sys_name='oa333', db_type=DatabaseType.oracle, db_ip='127.0.0.1',
                         db_port='1521', db_name='db', db_table_name='accounts', db_column_username='username',
                         db_column_password='password', db_password_encrypt_algorithm=EncryptAlgorithmType.md5)
    db_util.add_system(demo_system)
    for i in db_util.get_all_system():
        print i

    #update
    demo_system.db_type = DatabaseType.mysql
    demo_system.db_port = '3306'

    #request
    idd = demo_system.id
    print '____________________%d' % idd
    s =  db_util.get_system_by_id(idd)
    print s
    print '__ __ __ __ __ __ __ ___ ___%d' % idd

    #delete
    db_util.del_system(s)
    s =  db_util.get_system_by_id(idd)
    print s

if __name__ == '__main__':
    test()