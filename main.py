from get_data import get_data
from tg import send_message
import schedule
import time
from datetime import datetime


def job():
    try:
        free_spots_int = get_data()
    except:
        send_message("Error caught")
        return

    if free_spots_int > 0:
        send_message("Hey, you need to grab it right now!")
    else:
        print("Sorry, no free spots for now", datetime.now().strftime("%H:%M:%S"))


schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)


