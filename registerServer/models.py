from datetime import datetime
import os
from sqlalchemy.pool import SingletonThreadPool

__author__ = 'wm'

from sqlalchemy import Column, Integer, Sequence, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

Base = declarative_base()

class Serial(Base):
    __tablename__ = 'serial'
    id = Column(Integer, Sequence('system_id_seq'), primary_key=True)
    serial_key = Column(String(30), nullable=False, unique=True)
    user_name = Column(String(30), nullable=False)
    valid_end = Column(DateTime, nullable=True)

    def __repr__(self):
        return "<Serial(id=%d, serial_key='%s', user_name='%s', valid_end='%s')>" % (self.id, self.serial_key, self.user_name, self.valid_end)


class UseLog(Base):
    __tablename__ = 'use_log'
    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    log_time = Column(DateTime, nullable=True)

    def __repr__(self):
        return "<UseLog(%s %d)>" % self.message, self.log_time

@singleton
class DBUtil(object):

    session = None

    def __init__(self):
        sysinfo_db_engine = create_engine('sqlite:///' + os.path.dirname(__file__) + '/regDB', echo=False, connect_args={'check_same_thread':False}, poolclass=SingletonThreadPool)
        Base.metadata.create_all(sysinfo_db_engine)
        Session = sessionmaker(bind=sysinfo_db_engine)
        self.session = Session()

    def add_serial(self, serial):
        self.session.add(serial)
        self.session.commit()

    def check_serial(self, serial_key):
        res = self.session.query(Serial).filter(Serial.serial_key==serial_key).first()
        if res != None:
            vdays = (res.valid_end - datetime.now()).days
            if vdays > 0:
                return vdays
            else:
                return 0
        return -1

    def add_use_log(self, use_log):
        self.session.add(use_log)
        self.session.commit()

    def __del__(self):
        self.session.close()

if __name__ == "__main__":
    db_util = DBUtil()
    #use_log = UseLog(message='check XXX systems, total N, find X', log_time=datetime.now())
    #db_util.add_use_log(use_log)
    #cq_serial = Serial(user_name='cqxt', serial_key='adc9c08d7c', valid_end=datetime(2016, 4, 30))
    #db_util.add_serial(cq_serial)
    print db_util.check_serial('adc9c08d7c')