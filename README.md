# ChatBot

1. Running Chatbot
  * Clone this repository
  * Navigate to project location on your machine
  * In your terminal/CLI type `python manage.py runserver`
  * Open your browser and go to `127.0.0.1:8000` to see Chatbot
  
2. In case your server fails during start please try:
  * `python manage.py migrate`
  * or if you are getting database errors please run `python manage.py migrate --run-syncdb`
