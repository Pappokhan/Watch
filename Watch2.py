import time

while True:
    current_time = time.localtime()

    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    print(f"{hour:02}:{minute:02}:{second:02}")

    time.sleep(1)
