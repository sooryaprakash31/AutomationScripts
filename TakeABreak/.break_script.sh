#!/bin/bash

function breakmode(){
    read -p "Work time: " worktime
    read -p "Break time: " breaktime
    work=`python3 converter.py $worktime`
    break=`python3 converter.py $breaktime`
    echo "Carry on. I will notify you when it's break time"
    sleep $(($work-10))
    python3 desktop_notifier.py
    sleep 10s 
    sudo rtcwake -u -s $break -m mem
}