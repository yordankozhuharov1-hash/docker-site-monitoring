import requests
import time
from datetime import datetime

while True:
    with open("website.txt") as file:
        websites = file.readlines()

    for website in websites:
        website = website.strip()

        try:
            start = time.time()
            response = requests.get(website, timeout=5)
            end = time.time()

            response_time = round((end - start) * 1000, 2)

            status = "UP" if 200 <= response.status_code < 400 else "DOWN"

            log_line = (
                f"{datetime.now()} | "
                f"{website} | "
                f"{status} | "
                f"{response.status_code} | "
                f"{response_time} ms\n"
                f"--------------------\n"
            )

        except Exception as e:
            log_line = (
                f"{datetime.now()} | "
                f"{website} | "
                f"DOWN | ERROR | {e}\n"
            )

        with open("monitor.txt", "a", encoding="utf-8") as log:
            log.write(log_line)

        print(log_line.strip())

    time.sleep(60)