from sqlalchemy.orm import sessionmaker
from __setting__ import LOCAL_DB_File

__author__ = 'wm'

from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_enum34 import EnumType
from common import DatabaseType, EncryptAlgorithmType, singleton

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
        self.commit()

    def del_system_by_id(self, id):
        sys_info = self.session.query(SystemInfo).filter(SystemInfo.id==id)
        self.session.delete(sys_info)
        self.session.commit()

    def del_system(self, sys_info):
        self.session.delete(sys_info)
        self.session.commit()

    def __del__(self):
        self.session.close()