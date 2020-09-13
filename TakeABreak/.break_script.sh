#!/bin/bash

function breakmode(){
    zero=0
    read -p "Work time: " worktime
    work=`python3 converter.py $worktime`

    if [ $work == $zero ] 
    then
        echo "Invalid work time"
        return
    fi
    read -p "Break time: " breaktime  
    break=`python3 converter.py $breaktime`
    if [ $break == $zero ] 
    then
        echo "Invalid break time"
        return
    fi
    echo "Carry on. I will notify you when it's break time"
    while true;do
    sleep $(($work-10))
    python3 desktop_notifier.py
    sleep 10s
    sudo rtcwake -u -s $break -m mem
    done
}