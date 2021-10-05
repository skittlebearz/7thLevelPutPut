# 7thLevelPutPut
***
CS3450 minigolf web app project

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
Ensure python3 and pip3 are installed:

Clone GitHub repo:

    git clone https://github.com/skittlebearz/7thLevelPutPut.git

Setup up virtualenv

    virtualenv -p python3 <name>
    . <name>/bin/activate

Install dependencies:

    pip3 install -r requirements.txt

Run server:

    cd PutPutProject
    python3 manage.py runserver

## Unit testing

TBD unittesting?
   
## System testing

TBD

