import schedule
import time
import subprocess

def job():
    subprocess.call(['./bg.sh'])
    return

schedule.every().day.at("14:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(3600)
