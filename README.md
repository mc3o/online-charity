# online-charity

# Authors
- Joan Evans
- Stephen Ngugi
- Mathew M

## Setup and Installation  
To get the project .......  
#### Cloning the repository:  

##### Navigate into the folder  
 ```bash 
cd online-charity
```
##### Install and activate Virtual  
 ```bash 
 pipenv install requests 
 pipenv shell
```  
##### Install Dependencies  
 ```bash 
 pipenv install -r requirements.txt 
``` 
 ##### Add the following to the env file
  ```bash
 SECRET_KEY = your secret key
 DEBUG=TRUE
 DB_NAME=''
 DB_USER='database user name'
 DB_PASSWORD='database password'
 DB_HOST='127.0.0.1'
 MODE='dev'
 ALLOWED_HOSTS='*'
 DISABLE_COLLECTSTATIC=1
 EMAIL_USE_TLS = True
 EMAIL_HOST = 'smtp.gmail.com'
 EMAIL_PORT = 587
 EMAIL_HOST_USER = 'your email'
 EMAIL_HOST_PASSWORD = '<>'
 ```
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
 python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
```  
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.0.7](https://docs.djangoproject.com/en/3.0/)  
* [Heroku](https://heroku.com)  
* [Git](for version control)

## Known Bugs  
* There are no known bugs currently,though i encountered many of it during deployment,but i finally managed 

## Support and contact details
email: ngugimuthoni43@gmil.com, joanevans18@gmail.com, mathewalufwani@gmail.com 

  
