import psycopg2
import os

class dboperator:
    cur = 0
    conn = 0
    def __init__(self):
        self.conn = psycopg2.connect(database="hashdb", user="postgres", password="1qaz2wsx", host="127.0.0.1", port="5432")
        self.cur = self.conn.cursor()        
        
    def isInMd5table(self,md5Str):
        sql = "select count(*) from md5table where md5= \'" + md5Str + "\'"
        self.cur.execute(sql)
        resultSet = self.cur.fetchall()
        result = resultSet[0][0]
        if result > 0:
            return True
        else:
            return False
    
    def printList(self,DataList):
        for data in DataList:
            print(data)    

    def appendRecordToMd5table(self,Md5Str):
        sql = "insert into md5table values('" + Md5Str + "','u',current_date,'u')"
        self.cur.execute(sql)
        self.conn.commit()
        
    def asksha1table(self,DataList):
        return -1,-1,-1
    
    def getUnknownMd5List(self,Count):
        dataList = []
        sql = "select md5 from md5table where isweak='u' limit " + str(Count)
        self.cur.execute(sql)
        resultSet = self.cur.fetchall()
        for result in resultSet:
            dataList.append(result[0])
        return dataList
        
    def refreshMd5table(self,WeakList,StrongList):
        for weak in WeakList:
            sql = "update md5table set isweak='y',updatetime=current_date where md5='" + weak + "'"
            self.cur.execute(sql)
            self.conn.commit()
        for strong in StrongList:
            sql = "update md5table set isweak='n',updatetime=current_date where md5='" + strong + "'"
            self.cur.execute(sql)
            self.conn.commit()
        
    def askMd5table(self,DataList):
        weakList = []
        strongList = []
        unknownList = []
        
        for i in range(0,len(DataList)):
            sql = "select isweak from md5table where md5='" + DataList[i] + "'"
            self.cur.execute(sql)
            resultSet = self.cur.fetchall()
            if len(resultSet)>0:
                isweak = resultSet[0][0]
                if isweak == 'y':
                    weakList.append(i)
                elif isweak == 'n':
                    strongList.append(i)
                else:
                    unknownList.append(i)
            else:
                unknownList.append(i)
                self.appendRecordToMd5table(DataList[i])
        return weakList,strongList,len(unknownList)
