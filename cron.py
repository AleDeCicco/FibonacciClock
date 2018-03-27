import schedule
import time
import datetime

import os

def job():
    os.system("python clock.py")

os.system("python clock.py")
while 1:
    minutes = datetime.datetime.now().minute
    if minutes%5 == 0:
        break;

schedule.every(5).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
