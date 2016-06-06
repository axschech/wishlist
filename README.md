# Requirements
1. Python 2.7
2. MySQL 5.6

# To Run

1. virtualenv app
2. source app/bin/active
3. pip install -r requirements.txt
4. export FLASK_APP=app.py
5. flask run

# Current functionality
* There's only one test user, I'm working on adding users next
* POST: /refresh refreshes the test user's wishlist from steam (eventually this will support other platforms)
* GET: /games pulls down that list
