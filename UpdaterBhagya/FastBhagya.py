from pynput.keyboard import Key, Controller
import time
import random
import winsound

keyboard = Controller()

tm=6

time.sleep(3)
while True:
	winsound.Beep(2000, 800)
	print("Updating...")
	keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XA
	time.sleep(0.3)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	time.sleep(0.3)
	keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XB
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
	time.sleep(0.3)
	keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XF
	time.sleep(0.3)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	time.sleep(0.3)
	keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XG
	time.sleep(0.3)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	time.sleep(0.3)
	keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XH
	time.sleep(0.3)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	time.sleep(0.3)
	keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XI
	time.sleep(0.3)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	time.sleep(0.3)
	keyboard.type(str(random.randint(0,9))+str(random.randint(0,9)))#XJ
	time.sleep(0.3)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	time.sleep(0.3)
	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(tm/2)
	keyboard.press(Key.f5)
	keyboard.release(Key.f5)
	time.sleep(tm/2)
		
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

	time.sleep(tm/2)