#!/usr/bin/env bash
# set -e  Using failing grep...
set -x

grep rasp-net-monitor /etc/rc.local
if [[ $? == 1 ]]; then
    if (( $EUID != 0 )); then
        echo "Please run as root"
        exit
    fi
    sed -i -e '$i \/home/pi/rasp-net-monitor/rasp-net-monitor.py >> /tmp/rasp-net-monitor_stdout.log 2>&1 &\n' /etc/rc.local
else
    echo "rasp-net-monitor appears to be already installed:"
    echo ""
    echo "$ grep rasp-net-monitor /etc/rc.local"
    grep rasp-net-monitor /etc/rc.local
fi
