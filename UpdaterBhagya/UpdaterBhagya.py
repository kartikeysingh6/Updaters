from pynput.keyboard import Key, Controller
import time
import random
import winsound
import os
import pyautogui as pg
from datetime import datetime

keyboard = Controller()
os.startfile("BhagyaGUI.pyw")

alarm = ["09:00", "09:15", "09:30", "09:45", 
		"10:00", "10:15","10:30", "10:45",
		"11:00", "11:20", "11:40", 
		"12:00", "12:20", "12:40",
		"13:00", "13:20", "13:40",
		"14:00", "14:20", "14:40",
		"15:00", "15:20", "15:40",
		"16:00", "16:20", "16:40",
		"17:00", "17:20", "17:40",
		"18:00", "18:20", "18:40",
		"19:00", "19:20", "19:40",
		"20:00", "20:20", "20:40", 
		"21:00", "21:20", "21:40"]

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
	
	#Shutdown at 9:45 PM
	if curr=="21:45":
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

	print("Auto Pilot:"+str(pilot)+", Anti-Repeat:"+str(antirepeat),curr)
	
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
		ra=str(resA)+str(random.randint(0,9))#XA
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
		rb=str(resB)+str(random.randint(0,9))#XB
		keyboard.type(rb)
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		time.sleep(0.3)

		keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XC
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		time.sleep(0.3)
		
		keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XD
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		time.sleep(0.3)
		
		keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XE
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)

		keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XF
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)

		keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XG
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)

		keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XH
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)

		keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XI
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)

		keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XJ
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		
		#6.5 seconds so far
		time.sleep(30)
		keyboard.press(Key.space)
		keyboard.release(Key.space)
		
		time.sleep(15)
		keyboard.press(Key.f5)
		keyboard.release(Key.f5)
		time.sleep(15)
		
		for i in range(5):
			time.sleep(0.3)
			keyboard.press(Key.tab)
			keyboard.release(Key.tab)
		time.sleep(0.3)
		keyboard.press(Key.down)
		keyboard.release(Key.down)
		time.sleep(0.3)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)