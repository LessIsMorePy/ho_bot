import os
import pyautogui
from time import sleep


os.popen('notepad')
sleep(0.5)

file = open('file_test.txt', mode='r')
pyautogui.write(file.read(), interval=0.15)
file.close()

pyautogui.hotkey('ctrl', 'g')
sleep(0.5)

pyautogui.write('outfile.txt', interval=0.05)
sleep(0.5)

pyautogui.press('enter')
sleep(0.5)

pyautogui.hotkey('alt', 'f4')
