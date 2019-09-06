#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This small script has been created due to a Raspberry Pi that was losing WiFi connection after sometime.
# Objective is to get some logs about what might have happen and to make a reboot when it's happening.

# TODO #1 Use a decent logger to get 'output to file' / 'timestamp' / 'message level'
# TODO #2 Use 'iwlist' to get WiFi stats


import os  # for the 'system' command
import time  # Import the sleep function from the time module

PING_HOSTNAME = "www.free.fr"
DELAY_BEFORE_START = 900  # 15 min = Initial time (to avoid restarting every 5 minutes...)
DELAY_AFTER_SUCCESS = 300  # 5 min = delay after successful ping (was good => no need to do it again so soon)
DELAY_AFTER_FAILURE = 60  # delay after FAILED ping
MAX_FAILURES = 5  # Maximum consecutive failures allowed (in a row, separated by DELAY_AFTER_FAILURE seconds waiting)


def log_wireless_information():
    os.system("sudo iwlist wlan0 scan | grep 'Quality=\\|ESSID:\\|Address:\\|Frequency:'")


def main():
    log_wireless_information()
    time.sleep(DELAY_BEFORE_START)
    log_wireless_information()
    consecutive_failures = 0
    while consecutive_failures < MAX_FAILURES:
        response = 0
        while response == 0:
            response = os.system("ping -c 1 -w2 " + PING_HOSTNAME)
            if response == 0:
                print(PING_HOSTNAME + " is up and accessible!")
                consecutive_failures = 0
                time.sleep(DELAY_AFTER_SUCCESS)
            else:
                print(PING_HOSTNAME + " is not responding as expected!")
                log_wireless_information()

    consecutive_failures = consecutive_failures + 1
    time.sleep(DELAY_AFTER_FAILURE)

    minutes_down = (DELAY_AFTER_FAILURE * MAX_FAILURES) / 60
    print("It is " + str(minutes_down) + " minutes now that "
          + PING_HOSTNAME + " does not respond to ping. => restarting!!!")
    os.system("sudo shutdown -r now")


if __name__ == "__main__":
    main()
