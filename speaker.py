import subprocess
from tkinter import *
from gtts import gTTS
import sys
import os
from tempfile import TemporaryFile
import time

tmpfile = "tmp.mp3"
hist = []
histpoint = 0
histempty = True

def history_up(*event):
    global histpoint, histempty
    if hist == []:
        textentry.delete(0, 'end')
        return;
    if histempty:
        histpoint = 0
        histempty = False
    elif histpoint < len(hist)-1:
        histpoint += 1
    textentry.delete(0, 'end')
    textentry.insert(0,hist[histpoint])
    print(hist, histpoint, histempty)

def history_down(*event):
    global histpoint, histempty
    if hist == []:
        textentry.delete(0, 'end')
        return;
    if histpoint > 0:
        histpoint -= 1
        textentry.delete(0, 'end')
        textentry.insert(0,hist[histpoint])
        histempty = False
    else:
        histpoint = 0
        histempty = True
    if histempty:
        textentry.delete(0, 'end')
    print(hist, histpoint, histempty)

def history_drop(*event):
    global histpoint, histempty
    histpoint = 0
    histempty = True
    textentry.delete(0, 'end')

def show_entry_fields(*event):
    global hist, histpoint

    text=str(textentry.get())
    if text == "qq":
        print("Exiting...")
        sys.exit(0)
    if text == "":
        print("empty")
        return

    textentry.configure(state='disabled')
    textentry.update()
    tmp = TemporaryFile()
    ttsobj = gTTS(text=text, lang="de", slow=False)
    ttsobj.save(tmpfile)

    p = subprocess.Popen(['mpg123', '--reopen', '-w', 'tmp.wav', tmpfile])
    p.wait()
    p = subprocess.Popen(['aplay', "tmp.wav"])
    p.wait()

    #os.remove(tmpfile+"mp3")
    #os.remove(tmpfile+"wav")

    textentry.after(100, textentry.configure(state='normal'))
    textentry.update()
    hist.insert(0, text);
    histpoint = 0
    histempty = True
    textentry.delete(0, 'end')
    textentry.update()
    textentry.focus_set()
    textentry.update()

root = Tk()
root.attributes('-type', 'dialog')

textentry = Entry(root)
textentry.grid(row=0, column=0)
textentry.focus_set()
#Button(root, text='Show', command=show_entry_fields).grid(row=0, column=1, sticky=W, pady=4)
root.bind('<Tab>', show_entry_fields)
root.bind('<Return>', show_entry_fields)
root.bind('<KP_Enter>', show_entry_fields)
root.bind('<Up>', history_up)
root.bind('<Down>', history_down)
root.bind('<Escape>', history_drop)

mainloop( )
