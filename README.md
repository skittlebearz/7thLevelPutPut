# 7thLevelPutPut
***
CS3450 minigolf web app project

## IMPORTANT MILESTONE 3 INFO!	
Link to the folder containing:
- Sprint Plannings
- Sprint Retrospectives
- Standup Reports
- UI Manual testin write-ups
https://drive.google.com/drive/folders/1fASbTWxiv4f2l7xVIIaKykqDxwlskrE8?usp=sharing

After the project is build, you can run the following script that will run a handful of integrated unit tests:
    
    python manage.py test

## General Info
***
This repository contains all the documentation and code for the 7thLevelPutPut app. The code will largely be written in python and follow PEP8 standards. 

## Naming Polices
In accordance with PEP8 we will use spaces instead of tabs, CamelCase for classes, ALL_CAPS for constants, underscores in funciton and variable names, etc.

## Version-control procedures

- Project will be managed using Github
- Commits will be well labeled and informative as to what happened during that commit in case of bugs or version reverting.
- Code commits will be reviewed by at least one other team member before merged
- Functionality of web app must be built and tested before commiting to the main branch.
## Communication Policies
***
Project is managed via Discord. Team members use the #scrum-meeting channel to update their status on the days we don't meet via voice chat or zoom

## Tool stack description and setup procedure

Our tentative toolstack consists of:

Django - Web server framework using python  
https://www.djangoproject.com/

MySQL - Popular relational database  
https://www.mysql.com/

Bootstrap - Mobile-first frontend framework  
https://getbootstrap.com/

Font Awesome - Popular font and icon toolkit  
https://fontawesome.com/

## Build instructions
Three options. One is for windows(Reccomended, less database setup), one is a build script (ubuntu). The other is more manual in case the build script doesn't work(ubuntu).

### Windows Build Instructions
Clone repository

    git clone https://github.com/skittlebearz/7thLevelPutPut.git

Enter newly cloned repository

    cd 7thLevelPutPut

Ensure python virutal environment is installed

    pip install virtualenv

Create virutal environment

    virtualenv virtualputput

-------------------------------------    
Activate virutal environment
If using a linux/bash type shell

    source virutalputput/Scripts/activate

OR if using Powershell

    .\virtualputput\Scripts\activate
-------------------------------------

Ensure all dependencies are installed/accessible to virutal environment    

    pip install -r requirements.txt
    
Run the project migrate to initialize website

    python PutPutProject/manage.py migrate
    
Start up the website

    python PutPutProject/manage.py runserver
    
Now go to the starting point(dashboard) of the website http://127.0.0.1:8000/dashboard/

----------------------------------------------------------------

### (Ubuntu) Build Script Instructions
Clone GitHub repo and execute buildscript:

    git clone https://github.com/skittlebearz/7thLevelPutPut.git
    cd 7thLevelPutPut
    bash setup.sh <MySQL root password>
    . putputvenv/bin/activate
    python3 PutPutProject/manage.py runserver

----------------------------------------------------------------

### Manual Linux(Ubuntu) Instructions
Clone GitHub repo:

    git clone https://github.com/skittlebearz/7thLevelPutPut.git

Ensure dependencies are installed

    sudo apt install python3 python3-pip python3-dev python3.8-venv default-libmysqlclient-dev build-essential

Install MySQL

    wget -c https://repo.mysql.com//mysql-apt-config_0.8.19-1_all.deb
    dpkg -i mysql-apt-config_0.8.19-1_all.deb
    apt install mysql-server


Login to MySQL server as root
Create putput database

    CREATE DATABASE putput CHARACTER SET utf8;

Create django user

    CREATE USER 'django'@'localhost' IDENTIFIED BY <password>;
    GRANT ALL PRIVILEGES ON putput.* to django@localhost;

Create mysql.cnf file in root folder with following settings:

    [client]
    database = putput
    user = django 
    password = <password>
    default-character-set = utf8

Setup up virtualenv

    virtualenv -p python3 <name>
    . <name>/bin/activate

Install python modules:

    pip3 install -r requirements.txt

Run server:

    cd PutPutProject
    python3 manage.py runserver

## Unit testing

TBD unittesting?
   
## System testing

TBD

