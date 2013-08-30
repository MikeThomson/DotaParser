'''
Created on Aug 13, 2013

@author: Mike
'''
import pylab
import matplotlib.pyplot as plt
import sys
import bruno
import pprint
from time import sleep



if __name__ == '__main__':
	
	pp = pprint.PrettyPrinter(indent=4)
	
	if(len(sys.argv) > 1) :
		replay = sys.argv[1]
	else :
		exit(1);
	
	parser = bruno.BrunoParser('./bruno/')
	parser.parse(replay)
	
	players = parser.getPlayers()
	heroes = []
	for player in players :
		heroes.append(player["hero"])

	fig = plt.figure(1)
	ax = plt.axes()
	fig2 = plt.figure(2)
	
	ax2 = plt.axes()
	ax.set_title("Gold \n Click on legend line to toggle line on/off")
	ax2.set_title("CS \n Click on legend line to toggle line on/off")
	#leg.get_frame().set_alpha(0.4)
	
	lines = []
	levelLines = []
	
	data = {}
	levelData = {}
	csData = {}
	# maybe make this a function in bruno
	goldInfo = parser.getGold()
	csInfo = parser.getCs()
	for hero in heroes  :
		data[hero] = parser.totalEarnedOverTime(goldInfo, hero)
		for i in xrange(len(data[hero]["time"])) :
			data[hero]["time"][i] = parser.ticksToMinutes(data[hero]["time"][i])
			
		csData[hero] = parser.totalCsOverTime(csInfo, hero)
		for i in xrange(len(csData[hero]["time"])) :
			csData[hero]["time"][i] = parser.ticksToMinutes(csData[hero]["time"][i])
			
		line, = ax.plot(data[hero]["time"], data[hero]["gold"], label=parser.getPrettyName(hero))
		line2, = ax2.plot(csData[hero]["time"], csData[hero]["cs"], label=parser.getPrettyName(hero))
		lines.append(line)

	leg = ax.legend(loc='upper left', fancybox=True, shadow=True)

	lined = dict()
	for legline, origline in zip(leg.get_lines(), lines):
		legline.set_picker(5)  # 5 pts tolerance
		lined[legline] = origline

		
		
	
	def onpick(event):
		# on the pick event, find the orig line corresponding to the
		# legend proxy line, and toggle the visibility
		legline = event.artist
		origline = lined[legline]
		vis = not origline.get_visible()
		origline.set_visible(vis)
		# Change the alpha on the line in the legend so we can see what lines
		# have been toggled
		if vis:
			legline.set_alpha(1.0)
		else:
			legline.set_alpha(0.2)
		fig.canvas.draw()
		
	def onKey(event):
		print event.key
		#ax.frameon = False
		#ax.draw()
		#fig.canvas.draw()
		#fig2.canvas.draw()
		
	
	fig.canvas.mpl_connect('pick_event', onpick)
	fig.canvas.mpl_connect('key_press_event', onKey)

	plt.show()
	