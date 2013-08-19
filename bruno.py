'''
Created on Aug 14, 2013

@author: Mike
'''
import json
from operator import itemgetter

class BrunoParser(object):
	'''
	classdocs
	'''


	def __init__(self, jsonRootDir):
		'''
		Constructor
		'''
		self.jsonRootDir = "./json/"
		self.binaryPath = "./parser.exe"
		self.replay = None
		
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
	
	def parse(self): 
		if (self.isBinaryPathValid() is not True 
			or self.isJsonRootDirValid() is not True 
			or self.replay is None):
			return False
		# TODO run the parser exe
		return self.isJsonDirPopulated(self.replay)
	
	def getJsonForFile(self, filename):
		f = open('' + self.getReplayJsonPath() + filename + ".json", 'r')
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
	
	def ticksToMinutes(self, ticks):
		return ticks / 30.0 / 60.0
	
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
	
	def getLevelups(self):
		levelDicts = (self.getJsonForFile('levelups'))["leveluptimes"]
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