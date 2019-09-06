#!/usr/bin/env bash
# set -e  Using failing grep...
set +x

grep rasp-net-monitor /etc/rc.local
if [[ $? == 1 ]]; then
    echo "rasp-net-monitor not yet installed to /etc/rc.local for launch at startup..."
    if (( $EUID != 0 )); then
        echo "Must be root to install into rc.local... Please run with:"
        echo "sudo $0"
        exit
    fi
    sed -i -e '$i \/home/pi/rasp-net-monitor/rasp-net-monitor.py >> /tmp/rasp-net-monitor_stdout.log 2>&1 &\n' /etc/rc.local
    echo "Installed into rc.local - sed returned $?"
else
    echo "rasp-net-monitor appears to be already installed:"
    echo ""
    echo "$ grep rasp-net-monitor /etc/rc.local"
    grep rasp-net-monitor /etc/rc.local
fi
