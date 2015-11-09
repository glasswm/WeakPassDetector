import threading
import time 
from dboperator import dboperator
from raintableoperator import raintableoperator

def printList(DataList):
    for data in DataList:
        print(data)

def askDB(DataList,DataType):
    dbo = dboperator()
    if DataType == "md5":
        return dbo.askMd5table(DataList)
    elif DataType == "sha1":
        return dbo.askSha1table(DataList)
    else:
        return -1,-1,-1
    
def runDig(DataType,Count):
    rto = raintableoperator()
    dbo = dboperator()
    unknowList = []
    if DataType == "md5":
        while 1:
            unknowList = dbo.getUnknownMd5List(Count)
            printList(unknowList) 
            if len(unknowList)>0:
                weakList = rto.askRaintable(unknowList, "md5")
                strongList = set(unknowList) - set(weakList)
                dbo.refreshMd5table(weakList,strongList) 
            else:
                time.sleep(5)
                print("duang")               
    elif DataType == "sha1":
        pass
    else:
        pass
    
def startDig(DataType,Count):
    BruteHandler = threading.Thread(target=runDig,args=(DataType,Count))
    BruteHandler.start()

if __name__ == "__main__":
    DataList = []
    f = open("aa.txt",'r')
    fdata = f.readlines()
    for i in range(0,len(fdata)):
        fdata[i]=fdata[i].replace("\n","").replace("\r","")
        
#    askDB(fdata,"md5")
 #   print("finask")
    startDig("md5",3)
    
    
    
    
    