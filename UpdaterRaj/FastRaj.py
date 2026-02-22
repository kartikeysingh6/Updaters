from pynput.keyboard import Key, Controller
import time
import random
import winsound

keyboard = Controller()

tm=5

time.sleep(3)
while True:
	winsound.Beep(2000, 800)
	print("Updating...")
	keyboard.type("RA"+str(random.randint(0,9))+str(random.randint(0,9)))
	time.sleep(0.3)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	time.sleep(0.3)
	keyboard.type("RB"+str(random.randint(0,9))+str(random.randint(0,9)))
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
	time.sleep(0.3)
	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(tm/2)
	keyboard.press(Key.f5)
	keyboard.release(Key.f5)
	time.sleep(tm/2)
		
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

	time.sleep(tm/2)