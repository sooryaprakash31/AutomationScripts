#!/bin/bash

function breakmode(){
    read -p "Work time: " worktime
    read -p "Break time: " breaktime  
    echo "Carry on. I will notify you when it's break time"
    sleep $worktime
    python3 desktop_notifier.py
    sudo rtcwake -u -s $breaktime -m mem
}