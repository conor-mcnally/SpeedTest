import speedtest
import datetime
import time

s = speedtest.Speedtest()

while True:
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    downspeed = round((round(s.download()) / 1048576), 2)
    upspeed = round((round(s.upload()) / 1048576), 2)
    print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
    # 60 seconds sleep
    time.sleep(60)
