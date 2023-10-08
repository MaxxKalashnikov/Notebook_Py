import time
import os

try:
	opFile = open("notebook.txt", "r")
	readingFile = opFile.read()
except Exception:
	opFile = open("notebook.txt", "w")
	print("No default notebook was found, created one.")

while True:

	print("Now using file", os.path.basename(opFile.name))
	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit\n")

	selec = int(input("Please select one: "))
	if selec == 1:
		opFile = open(opFile.name, "r")
		readingFile = opFile.read()
		print(readingFile)
		opFile.close()
	elif selec == 2:
		opFile = open(opFile.name, "a")
		newNote = input("Write a new note: ")
		nowTime = time.strftime("%X %x")
		resultStr = newNote + ":::" + nowTime
		opFile.write(resultStr)
		opFile.close()
	elif selec == 3:
		opFile = open(opFile.name, "w")
		opFile.close()
		print("Notes deleted.")
	elif selec == 4:
		fileName = input("Give the name of the new file: ")
		try:
			opFile = open(fileName, "r")
			readingFile = opFile.read()
			opFile.close()
		except Exception:
			opFile = open(fileName, "w")
			print("No notebook with that name detected, created one.")
	elif selec == 5:
		print("Notebook shutting down, thank you.")
		break
	opFile.close()