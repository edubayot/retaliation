import urllib.request
import schedule
import time
import subprocess
import os
import random
import string

def job():
    fileName = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)]).''
    url = ''
    urllib.request.urlretrieve(url, '')
    subprocess.call(['./bg.sh'])
    return

schedule.every().day.at("14:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(3600)
