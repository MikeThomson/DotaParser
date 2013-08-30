'''
Created on Aug 14, 2013

@author: Mike
'''
import json
import os
import csv
from subprocess import call
from operator import itemgetter
from time import sleep
import sys
import imp

def main_is_frozen():
	return (hasattr(sys, "frozen") or # new py2exe
		hasattr(sys, "importers") # old py2exe
		or imp.is_frozen("__main__")) # tools/freeze

def get_main_dir():
	if main_is_frozen():
		return os.path.dirname(sys.executable)
	return os.path.dirname(sys.argv[0])

class BrunoParser(object):
	'''
	classdocs
	'''


	def __init__(self, jsonRootDir):
		'''
		Constructor
		'''
		'''
		if hasattr(sys,"frozen") and sys.frozen in ("windows_exe", "console_exe"):
			self.p=jpath.path(os.path.abspath(sys.executable)).dirname()
		else :
			self.p = os.path.abspath(os.path.realpath(__file__))
		'''
		self.p = get_main_dir()
		self.jsonRootDir = self.p + "/bruno/json/"
		self.binaryPath = self.p + "/bruno/DotaParser.exe"
		self.replay = None
		self.nameDict = None
		
	def setJsonRootDir(self, jsonRootDir):
		self.jsonRootDir = jsonRootDir
		pass
	
	def setBinaryPath(self, path):
		pass
	
	def isJsonRootDirValid(self):
		pass
	
	def isBinaryPathValid(self):
		pass
	
	def isJsonDirPopulated(self, replayId):
		pass
	
	def getPopulatedReplayList(self):
		pass
	
	def parse(self, replayPath): 
		#if (self.isBinaryPathValid() is not True 
		#	or self.isJsonRootDirValid() is not True 
		#	):
		
		#return False
		# TODO run the parser exe
		
		#os.chdir( 'c:\\documents and settings\\flow_model' )
		print call([os.path.abspath('' + self.binaryPath), 
				os.path.abspath(replayPath)], 
				cwd=os.path.abspath(self.p + "/bruno/"))
		self.replay = os.path.splitext(os.path.basename(replayPath))[0]
		
		return self.isJsonDirPopulated(self.replay)
	
	def getJsonForFile(self, filename):
		f = open(os.path.abspath('' + self.getReplayJsonPath() + filename + ".json"), 'r')
		ret = json.load(f)
		f.close()
		return ret
	
	def setReplayId(self, rid):
		self.replay = rid
		
	def getReplayJsonPath(self):
		return '' + self.jsonRootDir + '/' + self.replay + '/'
	
	def totalEarnedOverTime(self, inputData, hero):
		total = 0
		times = []
		totalGolds = []
		for ele in inputData :
			if(ele["hero"] == hero ) :
				times.append(int(ele["time"]))
				total += float(ele["gold"])
				totalGolds.append(total)
				
		return {"time" : times, "gold" : totalGolds}
	
	def totalCsOverTime(self, inputData, hero):
		total = 0
		times = []
		totalCs = []
		for ele in inputData :
			if(ele["hero"] == hero ) :
				times.append(int(ele["time"]))
				total += 1
				totalCs.append(total)
				
		return {"time" : times, "cs" : totalCs}
	
	def ticksToMinutes(self, ticks):
		return ticks / 30.0 / 60.0
	
	def getPrettyName(self, code):
		if self.nameDict == None :
			self.buildNameDict()
		if code in self.nameDict :
			return self.nameDict[code]
		else :
			return code
	
	def buildNameDict(self):
		self.nameDict = {}
		with open(os.path.abspath(self.p + "./bruno/dictionary.txt"), 'rb') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader :
				self.nameDict[row[0]] = row[1]
				
	def filterForHero(self, info, hero):
		retInfo = []
		for ele in info :
			if(ele["hero"] == hero) :
				retInfo.append(ele)
		return retInfo
		
	
	'''
	These are the methods used to actually get data from the json files
	'''
		
	def getBanPicks(self):
		pass
	
	def getBuildings(self):
		pass
	
	def getBuybacks(self):
		pass
		
	def getChat(self):
		pass
	
	def getCombatLog(self):
		pass
	
	def getCs(self):
		csDicts = (self.getJsonForFile('cs'))["cs"]
		return sorted(csDicts, key=itemgetter('replaytime'))
		pass
	
	def getDenies(self):
		pass
	
	def getGlyphs(self):
		pass
	
	def getGold(self):
		levelDicts = (self.getJsonForFile('gold'))["gold"]
		return sorted(levelDicts, key=itemgetter('replaytime'))
	
	def getHeroKills(self):
		pass
	
	def getItemTimes(self):
		pass
	
	def getLevelups(self, asNumber = False):
		levelDicts = (self.getJsonForFile('levelups'))["leveluptimes"]
		ret = []
		if asNumber :
			for ele in levelDicts :
				ele["level"] = int(ele["level"])
				ele["time"] = int(ele["time"])
				ret.append(ele)
			levelDicts = ret
		return sorted(levelDicts, key=itemgetter('replaytime'))
	
	def getPauses(self):
		pass
	
	def getPlayers(self):
		return (self.getJsonForFile('players'))["players"]
		pass
	
	def getRoshan(self):
		pass
	
	def getRunes(self):
		pass