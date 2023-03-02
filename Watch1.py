import datetime
import time

while True:
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"), end="", flush=True)

    time.sleep(1)
    
    print("\r", end="", flush=True)
