import datetime
import time
from main import init

while True:
    current_time = datetime.datetime.now()
    current_time_secs = int(current_time.strftime('%H')) * 3600 + int(current_time.strftime("%M")) * 60 + int(current_time.strftime('%S'))

    total_time_secs = 86400

    time.sleep(total_time_secs - current_time_secs)

    init()