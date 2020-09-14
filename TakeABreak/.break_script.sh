#!/bin/bash

function breakmode(){
    zero=0
    work=`python3 converter.py $1`
    if [ $work == $zero ] 
    then
        echo "Invalid work time"
        return
    fi
    break=`python3 converter.py $2`
    if [ $break == $zero ] 
    then
        echo "Invalid break time"
        return
    fi
    echo "Carry on. I will notify you when it's break time..."
    while true;do
    sleep $(($work-10))
    python3 desktop_notifier.py
    sleep 10s
    sudo rtcwake -u -s $break -m mem
    done
}