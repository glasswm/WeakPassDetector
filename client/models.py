__author__ = 'wm'

from sqlalchemy import Column, Integer, Sequence, String, create_engine, MetaData, Table, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_enum34 import EnumType
from common import DatabaseType, EncryptAlgorithmType, singleton
from sqlalchemy.orm import sessionmaker
from __setting__ import LOCAL_DB_File
import logging

Base = declarative_base()

class SystemInfo(Base):
    __tablename__ = 'systems'
    id = Column(Integer, Sequence('system_id_seq'), primary_key=True)
    sys_name = Column(String(30), nullable=False)
    db_type = Column(EnumType(DatabaseType), nullable=False)
    db_ip = Column(String(15), nullable=False)
    db_port = Column(String(8), nullable=False)
    db_name = Column(String(15), nullable=False)
    db_table_name = Column(String(15), nullable=False)
    db_column_username = Column(String(15), nullable=False)
    db_column_password = Column(String(15), nullable=False)
    db_password_encrypt_algorithm = Column(EnumType(EncryptAlgorithmType), nullable=False)

    def __repr__(self):
        return "<SystemInfo(id=%d, sys_name='%s', db_type='%s', db_name='%s')>" % (self.id, self.sys_name, self.db_type, self.db_name)


    def get_account_data(self, username, password):
        # Database Urls = "dialect+driver://username:password@host:port/database"
        if (self.db_type == DatabaseType.mysql):
            dialect = 'mysql'
            driver = 'mysqlconnector'
        elif (self.db_type == DatabaseType.oracle):
            dialect = 'oracle'
            driver = 'cx_oracle'
        else:
            logging.error(('unknown database type %s' % self.db_type))
            exit()
        sql_schema = '%s+%s://%s:%s@%s:%s/%s' % (dialect, driver, username, password, self.db_ip.replace(' ',''), self.db_port, self.db_name)
        engine = create_engine(sql_schema, echo=False)
        conn = engine.connect()
        metadata = MetaData()

        users = Table(self.db_table_name, metadata,
                      Column(self.db_column_username, String),
                      Column(self.db_column_password, String),
                      )

        s = select([users])
        result = conn.execute(s)
        res = []
        for row in result:
            #print row[self.db_column_username], row[self.db_column_password]
            res.append((row[self.db_column_username], row[self.db_column_password]))
        result.close()
        print res
        return res


@singleton
class DBUtil(object):

    session = None

    def __init__(self):
        sysinfo_db_engine = create_engine('sqlite:///' + LOCAL_DB_File, echo=False)
        Base.metadata.create_all(sysinfo_db_engine)
        Session = sessionmaker(bind=sysinfo_db_engine)
        self.session = Session()

    def add_system(self, system_info):
        self.session.add(system_info)
        self.session.commit()

    def get_all_system(self):
        res = self.session.query(SystemInfo).all()
        return res


    def get_system_by_id(self, id):
        res = self.session.query(SystemInfo).filter(SystemInfo.id==id).first()
        return res

    def update_system(self, SystemInfo):
        self.session.commit()

    def del_system_by_id(self, id):
        sys_info = self.session.query(SystemInfo).filter(SystemInfo.id==id)
        self.session.delete(sys_info)
        self.session.commit()

    def del_system(self, sys_info):
        self.session.delete(sys_info)
        self.session.commit()

    def __del__(self):
        self.session.close()