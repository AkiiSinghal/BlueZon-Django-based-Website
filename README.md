# BlueZon-Django-based-Website
It is PUBG Tournament website which paid matches are organised with prize money.

It is a Django based website with with full features of admin login for managing the site database and updates.

It also gives the feature of email verification of users.

## Command to run site
* Download the BlueZon folder and open cmd or terminal & Enter into the BlueZon folder.

* Install Django in your system.
  - pip install Django

* Enter into BlueZon folder.
  - cd BlueZon

* Make Migration by
  - python manage.py migrate
  - python manage.py makemigrations
  
* Add login admin user
  - py manage.py createsuperuser
  - Now enter your user name, email and password
  - **Note:** The Password will not be visible to you so enter it correctly.

* Run the server
  - py manage.py runserver
  
* Open Browser and type  **127.0.0.1:8000** to open your site

* You can also open the admin potal by opening **127.0.0.1:8000/admin** and using user admin user id.

* To activate email verification like features edit .[setting.py](https://github.com/AkiiSinghal/BlueZon-Django-based-Website/blob/master/BlueZon/gamers/settings.py)
  - Change the email id and password in 129 and 130 line respectively.
  
## Hosting
To host this website on the platform like AWS refer to the below link
* .[AWS Hosting](https://youtu.be/OLS0XD6oINA)

## ScreenShots
![Screenshot (37)](https://user-images.githubusercontent.com/42001728/61988375-fe73b400-b03d-11e9-8f9c-fa821717245b.png)
![Screenshot (38)](https://user-images.githubusercontent.com/42001728/61988372-fddb1d80-b03d-11e9-8f33-4367fdcea34e.png)
![Screenshot (36)](https://user-images.githubusercontent.com/42001728/61988374-fe73b400-b03d-11e9-966b-78efe81aefbc.png)
![Screenshot (35)](https://user-images.githubusercontent.com/42001728/61988373-fe73b400-b03d-11e9-8199-8b979bef79f4.png)
