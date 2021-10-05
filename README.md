# 7thLevelPutPut
***
CS3450 minigolf web app project

## General Info

This repository contains all the documentation and code for the 7thLevelPutPut app. The code will largely be written in python and follow PEP8 standards.

## Version-control procedures

- Project will be managed using Github
- Commits will be well labeled and informative as to what happened during that commit in case of bugs or version reverting.
- Code reviews will be held on commits to the main branch in attempt to lower the chance of bugs.
- Functionality of web app must be built and tested before commiting to the main branch.

## Tool stack description and setup procedure

Our tentative toolstack consists of:

### Python/Django and MySQL

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

