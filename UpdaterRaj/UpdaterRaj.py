from pynput.keyboard import Key, Controller
import time
import random
import winsound
import os
import pyautogui as pg
from datetime import datetime

keyboard = Controller()
os.startfile("RajGUI.pyw")

alarm = ["10:40", "11:00", "11:20", "11:40", "12:00", "12:20", "12:40", "13:00", "13:20", "13:40"
		,"14:00", "14:20", "14:40", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30"
		,"16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:20", "18:40", "19:00", "19:20"
		,"19:40", "20:00", "20:20", "20:40", "21:00"]

#Infinite Loop
while True:
	time.sleep(2)

	#Auto Pilot
	try:
		file = open("pilot.txt","r")
		pilot=int(file.read())
	except:
		pilot=1

	try:
		file = open("antirepeat.txt","r")
		antirepeat=int(file.read())
	except:
		antirepeat=0

	#Current date & time
	now = datetime.now()
	curr = now.strftime("%H:%M")
	
	#Shutdown at 9:05 PM
	if curr=="21:02":
		os.system("shutdown /s /t 1")

	#Extract valid inputs from lists
	try:
		file = open("lstA.txt","r")
		lestA=file.read()
	except:
		lestA=[0,1,2,3,4,5,6,7,8,9]
	try:
		file = open("lstB.txt","r")
		lestB=file.read()
	except:
		lestB=[0,1,2,3,4,5,6,7,8,9]

	print("Raj Auto Pilot:"+str(pilot)+", Anti-Repeat:"+str(antirepeat),curr)
	
	if curr in alarm and pilot==0:
		winsound.Beep(2000, 3000)
		time.sleep(60)				
	if curr in alarm and pilot:	
		winsound.Beep(2000, 2000)
		print("UPDATING FOR "+str(curr)+" ...")

		if antirepeat == 1:
			file = open("repeatA.txt","r")
			blockA=str(file.read())
			resA = random.choice([ele for ele in lestA if ele != blockA])
		else:
			resA = random.choice([ele for ele in lestA])
		with open("repeatA.txt", "w") as file:
				file.write(str(resA))
		ra="RA"+str(resA)+str(random.randint(0,9))
		keyboard.type(ra)
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		time.sleep(0.3)

		if antirepeat == 1:
			file = open("repeatB.txt","r")
			blockB=str(file.read())
			resB = random.choice([ele for ele in lestB if ele != blockB])
		else:
			resB = random.choice([ele for ele in lestB])
		with open("repeatB.txt", "w") as file:
				file.write(str(resB))
		rb="RB"+str(resB)+str(random.randint(0,9))
		keyboard.type(rb)
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		time.sleep(0.3)

		keyboard.type("RC"+str(random.randint(0,9))+str(random.randint(0,9)))
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		time.sleep(0.3)
		
		keyboard.type("RD"+str(random.randint(0,9))+str(random.randint(0,9)))
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		time.sleep(0.3)
		
		keyboard.type("RE"+str(random.randint(0,9))+str(random.randint(0,9)))
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		
		time.sleep(30)
		keyboard.press(Key.space)
		keyboard.release(Key.space)
		
		time.sleep(15)
		keyboard.press(Key.f5)
		keyboard.release(Key.f5)
		time.sleep(15)
		
		for i in range(6):
			time.sleep(0.3)
			keyboard.press(Key.tab)
			keyboard.release(Key.tab)
			
		time.sleep(0.3)
		keyboard.press(Key.down)
		keyboard.release(Key.down)
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		#Total time=75.5s