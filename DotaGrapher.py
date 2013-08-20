'''
Created on Aug 13, 2013

@author: Mike
'''
import pylab
import matplotlib.pyplot as plt
import bruno
import pprint




if __name__ == '__main__':
	
	parser = bruno.BrunoParser('./bruno/')
	parser.setJsonRootDir('./bruno/json/')
	parser.parse("bruno/278085711.dem")
	#parser.setReplayId('265874806')
	
	players = parser.getPlayers()
	heroes = []
	for player in players :
		heroes.append(player["hero"])
	
	#fig, (ax) = plt.subplots()
	#fig2 = plt.figure()
	fig = plt.figure()
	ax = plt.axes()
	
	ax2 = plt.axes((1,1,1,1))
	print ax is ax2
	ax.set_title('Click on legend line to toggle line on/off')
	#ax2.set_title('Boogy')
	#leg.get_frame().set_alpha(0.4)
	
	lines = []
	
	data = {}
	# maybe make this a function in bruno
	goldInfo = parser.getGold()
	for hero in heroes  :
		data[hero] = parser.totalEarnedOverTime(goldInfo, hero)
		for i in xrange(len(data[hero]["time"])) :
			data[hero]["time"][i] = parser.ticksToMinutes(data[hero]["time"][i])
			
		line, = ax.plot(data[hero]["time"], data[hero]["gold"], label=parser.getPrettyName(hero))
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
	