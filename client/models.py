# -*- coding: utf-8 -*-
import wx
import csv

__author__ = 'wm'

from sqlalchemy import Column, Integer, Sequence, String, create_engine, MetaData, Table, select, ForeignKey, \
    UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_enum34 import EnumType
from common import DatabaseType, EncryptAlgorithmType, singleton
from sqlalchemy.orm import sessionmaker, relationship, backref
from __setting__ import LOCAL_DB_File, account_limit
from mysql.connector.locales.eng import client_error
import logging

Base = declarative_base()

class SystemInfo(Base):
    __tablename__ = 'systems'
    id = Column(Integer, Sequence('system_id_seq'), primary_key=True)
    sys_name = Column(String(30), nullable=False)
    db_type = Column(EnumType(DatabaseType), nullable=True)
    db_ip = Column(String(15), nullable=True)
    db_port = Column(String(8), nullable=True)
    db_name = Column(String(15), nullable=False)
    db_table_name = Column(String(15), nullable=True)
    db_column_username = Column(String(15), nullable=True)
    db_column_password = Column(String(15), nullable=True)
    db_password_encrypt_algorithm = Column(EnumType(EncryptAlgorithmType), nullable=False)
    last_update_time = Column(DateTime, nullable=True)

    def __repr__(self):
        res =  u"<SystemInfo(id=%d, sys_name='%s', db_type='%s', db_name='%s', encrypt_alogorithm='%s')>" % (self.id, self.sys_name, self.db_type, self.db_name, self.db_password_encrypt_algorithm)
        return res.encode('utf-8')


    def get_csv_data(self, path):
        try:
            print 'Getting account data from csv file'
            csvfile = file(path, 'rb')
            reader = csv.reader(csvfile)
            res = []
            counter = 0
            if account_limit == -1:
                for line in reader:
                    if len(line) != 2:
                        pass
                    else:
                        res.append((line[0], line[1]))
            else:
                for line in reader:
                    if counter > account_limit:
                        break
                    if len(line) != 2:
                        pass
                    else:
                        res.append((line[0], line[1]))
                        counter += 1
            csvfile.close()
            print 'Get ' + str(len(res)) + ' records from csv file.'
        except Exception as e:
            print e.strerror
            warningStr = u"找不到对应的文件！"
            if e.strerror == 'No such file or directory':
                dlg = wx.MessageDialog(None, warningStr, u"提示", wx.OK | wx.ICON_QUESTION)
            else:
                dlg = wx.MessageDialog(None, e.strerror, u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            res = []
        return res


    def get_account_data(self, username, password):
        # Database Urls = "dialect+driver://username:password@host:port/database"
        try:
            print 'Getting accout data from system database'
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
            if account_limit == -1:
                s = select([users])
            else:
                s = select([users]).limit(account_limit)
            result = conn.execute(s)
            res = []
            for row in result:
                #print row[self.db_column_username], row[self.db_column_password]
                res.append((row[self.db_column_username], row[self.db_column_password]))
            result.close()
            print 'Get ' + str(len(res)) + ' records from database.'
        except Exception as e:
            print e.message
            dlg = wx.MessageDialog(None, e.message, u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            res = []
        return res

class Cryptograph(Base):
    __tablename__ = 'cryptograph'
    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    crypt_pass = Column(String, nullable=False)
    last_time = Column(Integer, nullable=False, default=0)
    system_id = Column(Integer, ForeignKey('systems.id'))

    system = relationship("SystemInfo", backref=backref('cryptograph', order_by=id))
    UniqueConstraint('user_name', 'system', name='uix_1')

    def __repr__(self):
        return "<Cryptograph(%s %s %d)>" % self.user_name, self.crypt_pass, self.last_time

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
        sys_info = self.session.query(SystemInfo).filter(SystemInfo.id==id).first()
        self.session.delete(sys_info)
        self.session.commit()

    def del_system(self, sys_info):
        self.session.delete(sys_info)
        self.session.commit()

    def get_crypt_by_systemID(self, sys_id):
        sys_info = self.session.query(SystemInfo).filter(SystemInfo.id==sys_id).first()
        crypt_list = []
        for i in sys_info.cryptograph:
            crypt_list.append((i.user_name, i.crypt_pass, i.last_time))
        return crypt_list

    #crypt_list = [(user_name1, crypt_pass1, last_time1), (user_name2, crypt_pass2, last_time2), ...]
    def set_crypt(self, sys_id, crypt_list):
        sys_info = self.session.query(SystemInfo).filter(SystemInfo.id==sys_id).first()
        for i in crypt_list:
            rec = self.session.query(Cryptograph).join(SystemInfo).filter(SystemInfo.id==sys_id, Cryptograph.user_name==i[0]).first()
            if rec != None:
                rec.crypt_pass = i[1]
                rec.last_time = i[2]
            else:
                rec = Cryptograph(user_name=i[0], crypt_pass=i[1], last_time=i[2], system=sys_info)
                self.session.add(rec)
        self.session.commit()

    def __del__(self):
        self.session.close()

if __name__ == "__main__":
    db_util = DBUtil()
    crypt_list = [('user1', '1242dsdf341', 0), ('user2', '1242dsdf342', 1), ('user3', '133342dsdf341', 10)]
    db_util.set_crypt(12, crypt_list)
    print db_util.get_crypt_by_systemID(12)