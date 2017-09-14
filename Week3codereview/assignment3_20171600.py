import pickle

dbfilename = 'assignment3_20171600.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
			scdb += [record]
		elif parse[0] == 'del':
			del2 = []
			index = 0
			for p in scdb:
				if p['Name'] == parse[1]:
					del2.append(index)
				index += 1
			for i in reversed(del2):
				scdb.pop(i)
		elif parse[0] == 'show':
			sortKey ='Name' if len(parse) == 1 else parse[1]
			showScoreDB(scdb, sortKey)
		elif parse[0] == 'quit':
			break
		elif parse[0] == 'find':
			for p in scdb:
				if p['Name'] == parse[1]:
					for attr in sorted(p):
						print(attr + "=" + p[attr], end=' ')
					print()
		elif parse[0] =='inc':
			for p in scdb:
				if p['Name'] == parse[1]:
					p['Score'] = int(p['Score'])
					p['Score'] += int(parse[2]) #오류발생...
		else:
			print("Invalid command: " + parse[0])
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

