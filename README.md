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

  
