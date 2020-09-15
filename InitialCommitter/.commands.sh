#!/bin/bash

function createrepo(){
     read -p "Github Username: " username
     read -s -p "Github Password: " password
     python3 /usr/bin/github_automate.py $1 $username $password
     cd
     cd /path/to/your/projects/folder/
     mkdir $1
     cd $1
     git init
     git remote add origin https://github.com/$username/$1.git
     touch README.MD
     git add .
     git commit -m "Initial Commit"
     git push -u origin master
     code .
     echo Project created and pushed to Github 
}
