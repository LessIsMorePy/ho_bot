"""
***************************************************
This script accomplish an automated task that consist
in open a note pad and start copying the text stored
in files with the extensions written in the glob
function.

At the end, the text will be saved
and finally the notepad it will be closed.

****************************************************
"""
import os
import pyautogui
from glob import glob
from time import sleep
from random import shuffle

# open notepad
os.popen('notepad')
sleep(0.5)

# read all files with the specified extension
files = glob('*.txt')

# random
shuffle(files)

# coping text
for path in files:

    file = open(path, mode='r')
    pyautogui.write(file.read(), interval=0.05)
    file.close()

# save and close notepad
pyautogui.hotkey('ctrl', 'g')
sleep(2)

pyautogui.write('outfile.txt', interval=0.5)
sleep(1)

pyautogui.press('enter')
sleep(0.5)

pyautogui.hotkey('alt', 'f4')
