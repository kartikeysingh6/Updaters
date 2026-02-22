from tkinter import *
import subprocess

root = Tk()
root.title('Raj Updater')
root.configure(bg="#add8e6")   # light blue

def pilot(val, label):
    file = open('pilot.txt', 'w+')
    file.write(str(val))
    file.close()
    filer = open('antirepeat.txt','r')
    valr=int(filer.read())
    filer.close()

    if val == 1 and valr ==1 :
        label['text'] = 'Auto Pilot: ON\nRepeat: BLOCK'
    if val == 0 and valr ==1 :
        label['text'] = 'Auto Pilot: OFF\nRepeat: BLOCK'
    if val == 1 and valr ==0 :
        label['text'] = 'Auto Pilot: ON\nRepeat: FREE'
    if val == 0 and valr ==0 :
        label['text'] = 'Auto Pilot: OFF\nRepeat: FREE'

def repeat(val, label):
    file = open('antirepeat.txt', 'w+')
    file.write(str(val))
    file.close()
    filep = open('pilot.txt','r')
    valp=int(filep.read())
    filep.close()

    if val == 1 and valp ==1 :
        label['text'] = 'Auto Pilot: ON\nRepeat: BLOCK'
    if val == 0 and valp ==1 :
        label['text'] = 'Auto Pilot: ON\nRepeat: FREE'
    if val == 1 and valp ==0 :
        label['text'] = 'Auto Pilot: OFF\nRepeat: BLOCK'
    if val == 0 and valp ==0 :
        label['text'] = 'Auto Pilot: OFF\nRepeat: FREE'

def exit_app():
    subprocess.run("taskkill /f /im python.exe /t", shell=True)
    subprocess.run("taskkill /f /im pythonw.exe /t", shell=True)

root.minsize(width=350, height=70)

label = Label(root, text='Welcome!', fg='black', font='Verdana 30 bold', bg="#add8e6")
label.pack()

f = Frame(root, bg="#add8e6")
f.pack(anchor='center', pady=5)

btn_style = {"bg": "#d0eaff"}  # light blue buttons

on = Button(f, text='Pilot ON', width=9, command=lambda: pilot(1, label), **btn_style)
off = Button(f, text='Pilot OFF', width=9, command=lambda: pilot(0, label), **btn_style)
blockon = Button(f, text='Repeat OFF', width=9, command=lambda: repeat(1, label), **btn_style)
blockoff = Button(f, text='Repeat ON', width=9, command=lambda: repeat(0, label), **btn_style)
exitb = Button(f, text='EXIT', width=6, fg='red', command=exit_app, **btn_style)

on.pack(side='left')
off.pack(side='left')
blockon.pack(side='right')
blockoff.pack(side='right')
exitb.pack(side='left')

root.mainloop()
