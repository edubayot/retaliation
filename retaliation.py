import requests
import mimetypes
import urllib
import schedule
import time
import subprocess
import os
import random
import string
from subprocess import Popen
import pyautogui
import threading

def job():
    url = 'https://picsum.photos/id/933/1920/1080'
    response =requests.head(url)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    fileName = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]) + extension
    urllib.request.urlretrieve(url, fileName)
    bgCommand = "gsettings set org.gnome.desktop.background picture-uri file://"+fileName
    bg = Popen(bgCommand.split(' '))
    threading.Thread(target=greetings).start()
    threading.Thread(target=crazyMouse).start()
    pyautogui.hotkey("winleft", "d")
    return

def greetings():

    sp = Popen(['espeak-ng', 'Hello Christiana, checkout your desktop, bitch!'])
    return

def crazyMouse():
     pyautogui.moveRel(100,100, 0.5)
     pyautogui.moveRel(-100,0, 0.5)
     pyautogui.moveRel(100, 0, 0.5)
     pyautogui.moveRel(0, -75, 0.5)
     pyautogui.moveRel(-75, 0, 0.5)
     return


schedule.every().day.at("14:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(3600)
