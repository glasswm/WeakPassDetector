__author__ = 'wm'

from sqlalchemy import create_engine, Table, Column, String, MetaData
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker

from common import DatabaseType, EncryptAlgorithmType
from models import SystemInfo, Base


def db_init():
    sysinfo_db_engine = create_engine('sqlite:///:memory:', echo=False)
    Base.metadata.create_all(sysinfo_db_engine)
    Session = sessionmaker(bind=sysinfo_db_engine)
    session = Session()
    demo_system = SystemInfo(sys_name='oa', db_type=DatabaseType.oracle, db_ip='127.0.0.1',
                         db_port='1521', db_name='db', db_table_name='accounts', db_column_username='username',
                         db_column_password='password', db_password_encrypt_algorithm=EncryptAlgorithmType.md5)
    session.add(demo_system)
    session.commit()

if __name__ == '__main__':
    db_init()
    engine = create_engine('mysql+mysqlconnector://root:7410@localhost:3306/wpd', echo=False)
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