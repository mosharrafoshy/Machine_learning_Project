import csv
import random
import math
import operator
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
 
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])
 
 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(4):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors
 
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response1 = int(neighbors[x][4])
		response2 = int(neighbors[x][5])
		response3 = int(neighbors[x][6])
		res1="Pre-Status"
		res2="On-time-Status"
		res3="Post-Status"
		if (response1==1):
			if res1 in classVotes:
				classVotes[res1] += 1
			else:
				classVotes[res1] = 1

		if (response2==1):
			if res2 in classVotes:
				classVotes[res2] += 1
			else: 
				classVotes[res2] = 1

		if (response3==1):
			if res3 in classVotes:
				classVotes[res3] += 1
			else:
				classVotes[res3] = 1

	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	split = 0.67
	#loadDataset('Debbie-Phase3-clean.csv', split, trainingSet, testSet)
	loadDataset('Debbie-Phase3-clean.csv', split, trainingSet, testSet)
	print 'Train set: ' + repr(len(trainingSet))
	print 'Test set: ' + repr(len(testSet))
	# generate predictions
	predictions=[]
	phase=[]
	k = 5
	l12=0
	l13=0
	l21=0
	l23=0
	l31=0
	l32=0
	l11=l22=l33=0
	pa1=pa2=pa3=0
	pp1=pp2=pp3=0
	maxt=0.0
	px1=[]
	py1=[]
	px2=[]
	py2=[]
	px3=[]
	py3=[]
	tx1=[]
	ty1=[]
	tx2=[]
	ty2=[]
	tx3=[]
	ty3=[]
	map_a_pre_lon = []
	map_a_on_lon = []
	map_a_post_lon = []
	map_a_pre_lat = []
	map_a_on_lat = []
	map_a_post_lat = []
	map_p_pre_lon = []
	map_p_on_lon = []
	map_p_post_lon = []
	map_p_pre_lat = []
	map_p_on_lat = []
	map_p_post_lat = []
	for x in range(len(trainingSet)):
		print str(trainingSet[x][3])
		print str(trainingSet[x][7]) + " " +str(trainingSet[x][8])
		if(float(trainingSet[x][7])!=-1 and float(trainingSet[x][8])!=-1):
			if(trainingSet[x][-1]=="Pre-Status"):
				map_p_pre_lon.append(float(trainingSet[x][7]))
				map_p_pre_lat.append(float(trainingSet[x][8]))
				map_a_pre_lon.append(float(trainingSet[x][7]))
				map_a_pre_lat.append(float(trainingSet[x][8]))
			if(trainingSet[x][-1]=="On-time-Status"):
				map_p_on_lon.append(float(trainingSet[x][7]))
				map_p_on_lat.append(float(trainingSet[x][8]))
				map_a_on_lon.append(float(trainingSet[x][7]))
				map_a_on_lat.append(float(trainingSet[x][8]))
			if(trainingSet[x][-1]=="Post-Status"):
				map_p_post_lon.append(float(trainingSet[x][7]))
				map_p_post_lat.append(float(trainingSet[x][8]))
				map_a_post_lon.append(float(trainingSet[x][7]))
				map_a_post_lat.append(float(trainingSet[x][8]))


	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)
		predictions.append(result)
		maxt=max(maxt,testSet[x][3])
		print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
		if(result==testSet[x][-1]):
			if(result=="Pre-Status"):
				l11+=1
			elif(result=="On-time-Status"):
				l22+=1
			else:
				l33+=1
			phase.append(result)
		elif(result!=testSet[x][-1] and testSet[x][-1]=="Pre-Status" and result=="On-time-Status"):
			l12+=1
		elif(result!=testSet[x][-1] and testSet[x][-1]=="Pre-Status" and result=="Post-Status"):
			l13+=1
		elif(result!=testSet[x][-1] and testSet[x][-1]=="On-time-Status" and result=="Pre-Status"):
			l21+=1
		elif(result!=testSet[x][-1] and testSet[x][-1]=="On-time-Status" and result=="Post-Status"):
			l23+=1
		elif(result!=testSet[x][-1] and testSet[x][-1]=="Post-Status" and result=="Pre-Status"):
			l31+=1
		elif(result!=testSet[x][-1] and testSet[x][-1]=="Post-Status" and result=="On-time-Status"):
			l32+=1

		if(result=="Pre-Status"):
			pp1+=1
			px1.append(testSet[x][3])
			py1.append(pp1)
			if(float(testSet[x][7])!=-1 and float(testSet[x][8])!=-1):
				map_p_pre_lon.append(float(testSet[x][7]))
				map_p_pre_lat.append(float(testSet[x][8]))
		if(result=="On-time-Status"):
			pp2+=1
			px2.append(testSet[x][3])
			py2.append(pp2)
			if(float(testSet[x][7])!=-1 and float(testSet[x][8])!=-1):
				map_p_on_lon.append(float(testSet[x][7]))
				map_p_on_lat.append(float(testSet[x][8]))
		if(result=="Post-Status"):
			pp3+=1
			px3.append(testSet[x][3])
			py3.append(pp3)
			if(float(testSet[x][7])!=-1 and float(testSet[x][8])!=-1):
				map_p_post_lon.append(float(testSet[x][7]))
				map_p_post_lat.append(float(testSet[x][8]))

		if(testSet[x][-1]=="Pre-Status"):
			pa1+=1
			tx1.append(testSet[x][3])
			ty1.append(pa1)
			if(float(testSet[x][7])!=-1 and float(testSet[x][8])!=-1):
				map_a_pre_lon.append(float(testSet[x][7]))
				map_a_pre_lat.append(float(testSet[x][8]))
		if(testSet[x][-1]=="On-time-Status"):
			pa2+=1
			tx2.append(testSet[x][3])
			ty2.append(pa2)
			if(float(testSet[x][7])!=-1 and float(testSet[x][8])!=-1):
				map_a_on_lon.append(float(testSet[x][7]))
				map_a_on_lat.append(float(testSet[x][8]))
		if(testSet[x][-1]=="Post-Status"):
			pa3+=1
			tx3.append(testSet[x][3])
			ty3.append(pa3)
			if(float(testSet[x][7])!=-1 and float(testSet[x][8])!=-1):
				map_a_post_lon.append(float(testSet[x][7]))
				map_a_post_lat.append(float(testSet[x][8]))
			
	print "Pre-Status = " + str(l11)
	print "On-time-Status = " + str(l22)
	print "Post-Status = " + str(l33)
	print "Pre-Status -> On-time-Status = " + str(l12)
	print "Pre-Status -> Post-Status = " + str(l13)
	print "On-time-Status -> Pre-Status = " + str(l21)
	print "On-time-Status -> Post-Status = " + str(l23)
	print "Post-Status -> Pre-Status = " + str(l31)
	print "Post-Status -> On-time-Status = " + str(l32)
	accuracy = getAccuracy(testSet, predictions)
  	print('Accuracy: ' + repr(accuracy) + '%')
	phase.reverse()
	p1=0
	p2=0
	p3=0
	phase_len=int(len(phase)*0.2)
	for i in range(phase_len):
			if(phase[i]=="Pre-Status"):
				p1+=1
			if(phase[i]=="On-time-Status"):
				p2+=1
			if(phase[i]=="Post-Status"):
				p3+=1
	p2=p2*2
	print "Length : " + str(phase_len) + " Pre-Status: " + str(p1) + " On-time-Status: " + str(p2) + " Post-Status: " + str(p3)
	if(p1==p2 and p1==p3):
		print('Phase Condition: Confuse')
	elif(p1==p2 and p1>p3):
		print('Phase Condition: Either Pre-Status Or On-time-Status')
	elif(p1==p3 and p1>p2):
		print('Phase Condition: Either Pre-Status Or Post-Status')
	elif(p2==p3 and p2>p1):
		print('Phase Condition: Either Post-Status Or On-time-Status')
	elif(p1>p2 and p1>p3):
		print('Phase Condition: Pre-Status')
	elif(p2>p1 and p2>p3):
		print('Phase Condition: On-time-Status')
	elif(p3>p1 and p3>p1):
		print('Phase Condition: Post-Status')
	labels = 'Pre-Status', 'On-Time-Status', 'Post-Status',
	sizes = [pa1, pa2, pa3]
	explode = (0, 0, 0)
	color = ("g", "r", "y")
	fig1, ax1 = plt.subplots()
	ax1.set_title("Actual Pie-Chart")
	ax1.pie(sizes, explode=explode, labels=labels, colors= color, autopct='%1.2f%%', shadow=False, startangle=180)
	ax1.axis('equal')

	labels = 'Pre-Status', 'On-time-Staus', 'Post-Status',
	sizes = [pp1, pp2, pp3]
	explode = (0, 0, 0)
	color = ("g", "r", "y")
	fig2, ax2 = plt.subplots()
	ax2.set_title("Predicted Pie-Chart")
	ax2.pie(sizes, explode=explode, labels=labels, colors= color, autopct='%1.2f%%', shadow=False, startangle=180)
	ax2.axis('equal')

	plt.show() 

	maxtw=max(pa1,max(pa2,pa3))
	fig3, ax3 = plt.subplots()
	ax3.set_xlabel('Time(Minutes)')
	ax3.set_ylabel('Number Of Tweets')
	ax3.set_title('Actual Axis Diagram')
	ax3.text(2, maxtw-2, r'Pre-Status : Green', color='g')
	ax3.text(2, maxtw-5, r'On-time-Status : red', color='r')
	ax3.text(2, maxtw-8, r'Post-Status : Yellow', color='y')
	ax3.plot(tx1, ty1, '-go', tx2, ty2, '-ro', tx3, ty3, '-yo')
	ax3.axis([0, maxt, 0, maxtw])

	maxtw1=max(pp1,max(pp2,pp3))
	fig4, ax4 = plt.subplots()
	ax4.set_xlabel('Time(Minutes)')
	ax4.set_ylabel('Number Of Tweets')
	ax4.set_title('Predicted Axis Diagram')
	ax4.text(2, maxtw1-2, r'Pre-Status : Green', color='g')
	ax4.text(2, maxtw1-5, r'On-time-Status : red', color='r')
	ax4.text(2, maxtw1-8, r'Post-Status : Yellow', color='y')
	ax4.plot(px1, py1, '-go', px2, py2, '-ro', px3, py3, '-yo')
	ax4.axis([0, maxt, 0, maxtw1])	

	plt.show()

	fig5, ax5 = plt.subplots()
	ax5.set_title("Actual Earth Map")
	map = Basemap(projection='robin', lon_0 = 10, lat_0 = 50)

	map.drawmapboundary(fill_color='blue')
	map.fillcontinents(color='white',lake_color='blue')
	map.drawcoastlines()

	
	xa1,ya1 = map(map_a_pre_lon, map_a_pre_lat)
	xa2,ya2 = map(map_a_on_lon, map_a_on_lat)
	xa3,ya3 = map(map_a_post_lon, map_a_post_lat)
	map.plot(xa1, ya1, 'g*', xa2, ya2, 'ro', xa3, ya3, 'y^', markersize=10)

	fig6, ax6 = plt.subplots()
	ax6.set_title("Predicted Earth Map")
	map = Basemap(projection='robin', lon_0 = 10, lat_0 = 50)

	map.drawmapboundary(fill_color='blue')
	map.fillcontinents(color='white',lake_color='blue')
	map.drawcoastlines()

	
	xp1,yp1 = map(map_p_pre_lon, map_p_pre_lat)
	xp2,yp2 = map(map_p_on_lon, map_p_on_lat)
	xp3,yp3 = map(map_p_post_lon, map_p_post_lat)
	map.plot(xp1, yp1, 'g*', xp2, yp2, 'ro', xp3, yp3, 'y^', markersize=10)
	plt.show()

main()
