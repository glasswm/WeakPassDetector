import os

class raintableoperator:
    md5FilenameList = []
    sha1FilenameList = []
    
    def __init__(self):
        self.initMd5FilenameList()
        self.initSha1FilenameList()

    def initMd5FilenameList(self):
        self.md5FilenameList = []
        self.md5FilenameList.append("md5_numeric#1-8_0_300x4000000_oxid#000.rt") 
        
    def initSha1FilenameList(self):
        pass
    
    def getMd5FilelistStr(self):
        result = " "
        for md5Filename in self.md5FilenameList:
            result = result + md5Filename + " "
        return result 
    
    def getSha1FilelistStr(self):
        result = " "
        for sha1Filename in self.sha1FilenameList:
            result = result + sha1Filename + " "
        return result 
    
    def writeListToFile(self,DataList,Filename):
        f = open(Filename,'w')
        try:
            for data in DataList:
                f.write(data + "\r\n")
        finally:
            f.close()
            
    def printList(self,DataList):
        for data in DataList:
            print(data)
    
    def askRaintable(self,DataList,HashType):
        weakList = []
        tempFilename = "/tmp/temp.txt"
        if HashType == "md5":
            self.writeListToFile(DataList,tempFilename)
            cmdStr = "./rcrack" + self.getMd5FilelistStr() + "-l " + tempFilename + "|grep \"plaintext of\" "
            resultList = os.popen(cmdStr).readlines()  
            for record in resultList:
                elements = record.split(" ")
                weakList.append(elements[2])                
        elif HashType == "sha1":
            self.writeListToFile(DataList,tempFilename)
            cmdStr = "./rcrack" + self.getSha1FilelistStr() + "-l " + tempFilename + "|grep \"plaintext of\" "
            resultList = os.popen(cmdStr).readlines()  
            for record in resultList:
                elements = record.split(" ")
                weakList.append(elements[2])  
        else:
            pass   
        return weakList
    
  