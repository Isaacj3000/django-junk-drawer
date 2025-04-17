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
refer to .env.example for variable values 

### In IDE Terminal run:
    createbd junkdrawer 
    python3 manage.py migrate
    python3 manage.py runserver

### Create a branch to start working on your sections
    git checkout -b branch_name

### Database Configuration
1. Create your database first: createdb junkdrawer
2. Replace user, password, and secret key with your own values
Note: Never use these example values in production!

DB_NAME=junkdrawer
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# Django Configuration
SECRET_KEY=your-django-secret-key

    
