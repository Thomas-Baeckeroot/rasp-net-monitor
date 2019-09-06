#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os  # for the 'system' command
import time  # Import the sleep function from the time module

PING_HOSTNAME = "www.free.fr"
DELAY_BEFORE_START = 900  # 15 min = Initial time (to avoid restarting every 5 minutes...)
DELAY_AFTER_SUCCESS = 300  # 5 min = delay after successful ping (was good => no need to do it again so soon)
DELAY_AFTER_FAILURE = 60  # delay after FAILED ping
MAX_FAILURES = 5  # Maximum consecutives failures allowed (in a row)


def main():
    time.sleep(DELAY_BEFORE_START)
    consecutive_failures = 0
    while consecutive_failures < MAX_FAILURES:
        response = 0
        while (response == 0):
            response = os.system("ping -c 1 -w2 " + PING_HOSTNAME)
            if response == 0:
                print(PING_HOSTNAME + " is up!")
                consecutive_failures = 0
                time.sleep(DELAY_AFTER_SUCCESS)
            else:
                print(PING_HOSTNAME + " is down!")
        
        consecutive_failures = consecutive_failures + 1
        time.sleep(DELAY_AFTER_FAILURE)
        
    print("It is " + str((DELAY_AFTER_FAILURE * MAX_FAILURES) / 60) + " minutes now that " + PING_HOSTNAME + " does not respond to ping. => restarting!!!")
    os.system("sudo shutdown -r now")


if __name__ == "__main__":
    main()
