# Insta-Clone!!

### 7th Dec. 2021

## Author

[Derrick Macharia](https://github.com/derrickmacharia)

# Description
This is a Python Application where a user(s) can view  a photo, search through category and view according to the location taken.

##  Live Link 
 (https://bazenga-art.herokuapp.com/)

## Screenshots
###### Home page
<img src="static/images/Screenshot (1).png">

###### Image Details
<img src="static/images/Screenshot (2).png">

###### Search by Category
 <img src="static/images/Screenshot (3).png">

###### Search by Location
<img src="static/images/Screenshot (4).png">




## User Story 
* View different photos from the Application
* Click a single image to expand it and view the details of that post
* Search for images by different categories.
* Copy a link to the photo.
* Filter photos based on the location.

## Setup and Installation 

##### Clone the repository: 
 ```bash
 git@github.com:derrickmacharia/The-Collector.git
```
##### Navigate into the folder and install requirements 
 ```bash
cd Insta-Clone pip install -r requirements.txt
```
##### Install and activate Virtual 
 ```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations instapp
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application 
 ```bash
 python manage.py runserver
```
##### Running the application 
 ```bash
 python manage.py server
```
##### Testing the application 
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.

## Technology used 
* [Python3.8](https://www.python.org/)
* [Django==3.2.7](https://docs.djangoproject.com/en/2.2/)
* [Heroku](https://heroku.com)

## Known Bugs 
* There are no known bugs


## Support and contact details
For more information,comments or clarification contact on derrick.macharia@student.moringaschool.com


### License
*MIT License*
MIT License

    Copyright (c) 2021 Derrick Macharia
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

Copyright (c) {2021} **Derrick Macharia**