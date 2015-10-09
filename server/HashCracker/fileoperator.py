import os
import time

def getDataStr():
	dataStr = time.strftime("%Y-%m-%d",time.localtime())
	return dataStr

def getTimeStr():
	timeStr = time.strftime("[%Y-%m-%d %H:%M:%S] ",time.localtime())
	return timeStr

def readListFromFile(fileName):
	f = open(fileName,"r")
	try:		
		fData = f.readlines()
		for i in range(0,len(fData)):
			fData[i] = fData[i].replace("\n","")			
	finally:		
		f.close()
	return fData

def appendListToFile(fileName,inputList):
	f = open(fileName,"a")
	try:
		for line in inputList:
			f.write(line + "\n")
	finally:		
		f.close()

def appendRecordToFile(fileName,inputdata):
	f = open(fileName,"a")
	try:
		f.write(inputdata + "\n")
	finally:		
		f.close()

def writeLog(logData):
	logFilename = os.getcwd() + "\\log\\runtimelog.log"
	logDataWithTime = getTimeStr() + logData
	self.appendRecordToFile(logFilename,logDataWithTime)