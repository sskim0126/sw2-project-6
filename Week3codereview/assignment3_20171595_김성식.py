import pickle
import copy

dbfilename = 'assignment3.dat'


def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb = pickle.load(fH)
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
	while (True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			try:
				record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
			except:
				print("Enter a right command")
			else:
				scdb += [record]
		elif parse[0] == 'del':
			try:
				exception = parse[1]
			except:
				print("Enter a right command")
			else:
				Copy_scdb = copy.deepcopy(scdb)
				for p in Copy_scdb:
					if p['Name'] == parse[1]:
						scdb.remove(p)
		elif parse[0] == 'show':
			sortKey = 'Name' if len(parse) == 1 else parse[1]
			try:
				showScoreDB(scdb, sortKey)
			except:
				print("Enter a right command")
		elif parse[0] == 'find':
			try:
				exception = parse[1]
			except:
				print('Enter a right command')
			else:
				for p in scdb:
					if p['Name'] == parse[1]:
						for attr in sorted(p):
							print(attr + "=" + p[attr], end=' ')
						print()
		elif parse[0] == 'inc':
			try:
				exception1 = parse[1]
				exception2 = int(parse[2])
			except:
				print("Enter a right command")
			else:
				for p in scdb:
					if p['Name'] == parse[1]:
						p['Score'] += int(parse[2])
		elif parse[0] == 'quit':
			break
		else:
			print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + str(p[attr]), end=' ')
		print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
