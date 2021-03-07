# Steps to run project

- First install 'requirements.txt' 
- Run migration commands

        python manage.py makemigrations
        python manage.py migrate

- Then run project by

        python manage.py runserver

# Api endpoints 

- Login Api to generate access token - (POST api) please pass token as authorization 

        http://127.0.0.1:8000/api/login/

- For User List - Get api 

        http://localhost:8000/api/users/

- To get user by id like id=1 and update it

        http://localhost:8000/api/users/1

- To Create user - POST
        
        http://localhost:8000/api/users/