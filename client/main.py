__author__ = 'wm'

from common import DatabaseType, EncryptAlgorithmType
from models import SystemInfo, DBUtil


def test_get_account_data_mysql():
    db_util = DBUtil()

    test_system = SystemInfo(sys_name='test_system', db_type=DatabaseType.mysql, db_ip='127.0.0.1',
                         db_port='3306', db_name='wpd', db_table_name='user_table', db_column_username='user_id',
                         db_column_password='user_password', db_password_encrypt_algorithm=EncryptAlgorithmType.md5)

    db_util.add_system(test_system)
    print '____________________%d' % test_system.id
    test_system.get_account_data(username='root', password='7410')

def test_get_account_data_oracle():
    db_util = DBUtil()

    test_system = SystemInfo(sys_name='test_system2', db_type=DatabaseType.oracle, db_ip='192.168.238.130',
                         db_port='1521', db_name='ora11g', db_table_name='PM_BID_PROJECT_INFO', db_column_username='PRJ_NO',
                         db_column_password='BID_NAME', db_password_encrypt_algorithm=EncryptAlgorithmType.md5)

    db_util.add_system(test_system)
    print '____________________%d' % test_system.id
    test_system.get_account_data(username='SGCIS', password='sgcis')


def test_sysinfo_manage():
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
    test_get_account_data_oracle()

    #test end by jack,new test