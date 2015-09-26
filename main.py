from __setting__ import LOCAL_DB_File

__author__ = 'wm'

from sqlalchemy import create_engine, Table, Column, String, MetaData
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker

from common import DatabaseType, EncryptAlgorithmType
from models import SystemInfo, Base, DBUtil


def db_init():
    sysinfo_db_engine = create_engine('sqlite:///' + LOCAL_DB_File, echo=False)
    Base.metadata.create_all(sysinfo_db_engine)
    Session = sessionmaker(bind=sysinfo_db_engine)
    session = Session()
    demo_system = SystemInfo(sys_name='oa', db_type=DatabaseType.oracle, db_ip='127.0.0.1',
                         db_port='1521', db_name='db', db_table_name='accounts', db_column_username='username',
                         db_column_password='password', db_password_encrypt_algorithm=EncryptAlgorithmType.md5)
    session.add(demo_system)
    session.commit()


def test():
    engine = create_engine('mysql+mysqlconnector://root:7410@192.168.44.133:3306/wpd', echo=False)
    conn = engine.connect()
    metadata = MetaData()

    users = Table('user_table', metadata,
                  Column('user_id', String),
                  Column('user_password', String),
                  )

    s = select([users])
    result = conn.execute(s)
    for row in result:
        print row
    result.close()

if __name__ == '__main__':
    db_util = DBUtil()
    demo_system = SystemInfo(sys_name='oa333', db_type=DatabaseType.oracle, db_ip='127.0.0.1',
                         db_port='1521', db_name='db', db_table_name='accounts', db_column_username='username',
                         db_column_password='password', db_password_encrypt_algorithm=EncryptAlgorithmType.md5)
    db_util.add_system(demo_system)
    for i in db_util.get_all_system():
        print i

    demo_system.db_type = DatabaseType.mysql
    demo_system.db_port = '3306'

    idd = demo_system.id

    print '____________________%d' % idd
    s =  db_util.get_system_by_id(idd)
    print s
    print '__ __ __ __ __ __ __ ___ ___%d' % idd
    db_util.del_system(s)
    s =  db_util.get_system_by_id(idd)
    print s