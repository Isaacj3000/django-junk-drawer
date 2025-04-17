# Getting Started
### Clone repo to your local machine
    git clone https://github.com/Cpreza24/django-junk-drawer.git

### Install Django
    pipenv install django
wait for terminal to show 
-> django-junk-drawer git (main) then run: (enters virtual enviornment)
    
    pipenv shell

### Open project in your IDE (depending on your IDE)
    cursor . 
    code .

### Inside IDE teriminal install dependancies 
    pipenv install

### Create your ENV file
    touch .env
refer to .env.example for variable values 
add your .env to .gitignore

### In IDE Terminal run:
    1. createdb junkdrawer 
    2. python3 manage.py migrate
    3. python3 manage.py runserver

### Check Database connection (optional)
In the terminal run 
    
    1. psql -b junkdrawer
    2. \dt 

Displays the tables created by Django 
q returns you to Postgres shell
exit or \q quits the Postgres CLI 


### Create a branch to start working on your sections
    git checkout -b branch_name

