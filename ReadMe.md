## OpenExchangeTest
### Requirements
> * Python3.6
> * Django

Note the project uses sqlite3 as the db

### Installation
* clone the project and create an env
* create and activate a virtualenv and run ```pip install -r requirements.txt```
* create migrations by running ```./manage.py makemigrations && ./manage.py migrate```
* proceed to create a user with the command ```./manage.py createsuperuser```
* you can seed data by running the script ```seed.py```  
* run the app via ```./manage.py runserver``` and access your app on http://localhost:8000

### API
#### obtaining an access token
>POST
> 
> http://localhost:8000/api/token/
> ```
> {
>    "username":"username",
>    "password":"password"
> }
> ```
#### Refresh token
> POST
> 
> http://localhost:8000/api/token/refresh/
> ```
> {
>    "refresh":"refresh_token",
> }
> ```
> 
#### Get All Available Currency Codes - *does not require authentication*
> GET
> 
> http://localhost:8000/api/currencies

#### currency Conversion - *requires authentication*
> POST
> 
> http://localhost:8000/api/currency/convert
> #### sample request 
> ```
> {
>	 "base_currency" : "USD",
>	 "target_currency" : "KES",
>	 "amount" : 100
> }
> ```
> #### sample response 
> ```
>
> {
>    "base_currency": "USD",
>    "target_currency": "KES",
>    "amount": 10970.16,
>    "rate": 109.7016
> }
> ```


> NOTE: all authenticated routes require the JWT access token passed on the headers ie ```"Authorization": "Bearer access_token"```

### Enjoy :smile: 