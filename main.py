__author__ = 'wm'

from sqlalchemy import create_engine, Table, Column, Integer, String, Text, MetaData, ForeignKey
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_enum34 import EnumType

from base import singleton, DatabaseType, EncryptAlgorithmType

Base = declarative_base()

@singleton
class DBUtil(object):
    pass

class SystemInfo(Base):
    __tablename__ = 'systems'
    id = Column(Integer, primary_key=True)
    sys_name = Column(String, nullable=False)
    db_type = Column(EnumType(DatabaseType), nullable=False)
    db_ip = Column(String, nullable=False)
    db_port = Column(String, nullable=False)
    db_name = Column(String, nullable=False)
    db_table_name = Column(String, nullable=False)
    db_column_username = Column(String, nullable=False)
    db_column_password = Column(String, nullable=False)
    db_password_encrypt_algorithm = Column(EnumType(EncryptAlgorithmType), nullable=False)


    def __repr__(self):
       return "<SystemInfo(sys_name='%s', db_type='%s', db_name='%s')>" % (self.sys_name, self.db_type, self.db_name)

sysinfo_db_engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(sysinfo_db_engine)


engine = create_engine('mysql+mysqlconnector://root:7410@localhost:3306/wpd', echo=True)
conn = engine.connect()
metadata = MetaData()


# users = Table('user_table', metadata,
#               Column('id', Integer, primary_key=True),
#               Column('user_id', String),
#               Column('user_password', String),
#               Column('other', Text),
#               )

users = Table('user_table', metadata,
              Column('user_id', String),
              Column('user_password', String),
              )


s = select([users])
result = conn.execute(s)
for row in result:
    print row

result.close()