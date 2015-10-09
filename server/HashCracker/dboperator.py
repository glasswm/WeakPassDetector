import sqlite3
import os

def askDB(md5List):    
    weakList = []
    strongList = []
    unknowList = []    
    dbDir = os.getcwd() + "\\db\\knowledge.db"
    con = sqlite3.connect(dbDir)
    cur = con.cursor()
    for md5Str in md5List:
        if isInTable(md5Str,"weakmd5",cur):
            weakList.append(md5Str)
        elif isInTable(md5Str,"strongmd5",cur):
            strongList.append(md5Str)
        else:
            unknowList.append(md5Str)
    return weakList,strongList,unknowList

def isInTable(md5Str,tableName,cur):
    sql = "select count(*) from " + tableName + " where md5=\"" + md5Str + "\""
    cur.execute(sql)
    datacount = cur.fetchall()[0][0]
    if datacount > 0:
        return True
    else:
        return False

def updateTable(md5Str,tableName):
    dbDir = os.getcwd() + "\\db\\knowledge.db"
    con = sqlite3.connect(dbDir)
    cur = con.cursor()
    if isInTable(md5Str,tableName,cur):
        pass
    else:
        sql = "insert into " + tableName + " values(\"" + md5Str + "\")"
        print(sql)
        cur.execute(sql)
    con.commit()
    con.close()    

def showTable(tableName):
    dbDir = os.getcwd() + "\\db\\knowledge.db"
    con = sqlite3.connect(dbDir)
    cur = con.cursor()    
    sql = "select md5 from " + tableName 
    cur.execute(sql)
    resultset = cur.fetchall()
    for record in resultset:
        print(record[0])   
    con.close()

def initDB():
    dbDir = os.getcwd() + "\\db\\knowledge.db"
    con = sqlite3.connect(dbDir)
    cur = con.cursor()
    cur.execute("create table weakmd5 (md5 varchar(100))")
    cur.execute("create table strongmd5 (md5 varchar(100))")    
    for i in range(0,100):
        sql = "insert into weakmd5 values(\"" + str(i) + "\")"
        cur.execute(sql)
    con.commit()    
    for i in range(1000,2000):
        sql = "insert into strongmd5 values(\"" + str(i) + "\")"
        cur.execute(sql)
    con.commit()    
    con.close()
    
def test():
    md5List = []
    md5List.append("1")
    md5List.append("10")
    md5List.append("999")
    md5List.append("1000")
    md5List.append("1234")
    md5List.append("4356")
    md5List.append("9999")
    md5List.append("344324")
    md5List.append("34447")
    w,s,u = askDB(md5List)
    print w
    print s
    print u    
    
