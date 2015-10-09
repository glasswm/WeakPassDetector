import sqlite3
import os
import threading

def askDB(dataType,dataList):
    if dataType == "md5":
        return askMd5DB(dataList)
    elif dataType == "sha1":
        return askSha1DB(dataList)
    else:
        return -1,-1,-1    

def askSha1DB(sha1List):
    pass

def askMd5DB(md5List):
    weakList = []
    strongList = []
    unknowList = []
    dbDir = os.getcwd() + "\\db\\knowledge.db"
    con = sqlite3.connect(dbDir)
    cur = con.cursor()
    for i in range(0,len(md5List)):
        if isInTable(md5List[i],"weakmd5",cur):
            weakList.append(i)
        elif isInTable(md5List[i],"strongmd5",cur):
            strongList.append(i)
        else:
            unknowList.append(md5List[i])

    md5BruteHandler = threading.Thread(target=bruteWeakMd5List,args=(unknowList,))
    md5BruteHandler.start()
    return weakList,strongList,len(unknowList)

def bruteWeakMd5List(md5StrList):
    for md5Str in md5StrList:
        isWeakMd5(md5Str)
    
def isWeakMd5(md5Str):
    rainTableName = "md5_numeric#1-8_0_300x4000000_oxid#000.rt"
    cmd = "rcrack.exe " + rainTableName + " -h " + md5Str    
    result = os.popen(cmd).readlines()  

    if isMatch("plaintext of",result):
        updateTable(md5Str, "weakmd5")
        return True
    else:
        updateTable(md5Str, "strongmd5")
        return False

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
    con.commit()    
    con.close()
  
def isMatch(re,dataList):
    for data in dataList:
        if data.count(re) > 0:
            return True
        else:
            pass
    return False

#if __name__ == '__main__':
 #  initDB()
 #   dataList = []
 #   dataList.append("d09bf41544a3365a46c9077ebb5e35c3")
 #   dataList.append("67c6a1e7ce56d3d6fa748ab6d9af3fd7")
 #   dataList.append("8e296a067a37563370ded05f5a3bf3ec")
 #   w,s,u = askDB("md5",dataList)
 #   print(w)
 #   print(s)
 #   print(u)
