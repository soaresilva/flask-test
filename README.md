# flask-test
Using Flask to create an event registration form.

### Instructions

1) Install dependencies by running `pip3 install -r requirements.txt`.
2) On the command line, run `source .env` to load environment variables from the .env file.
3) Open config.py and configure your MySQL connection info.
4) Run `python3 bootstrap_db.py` to create MySQL database and tables. Requires a [connector](https://www.mysql.com/products/connector/). If, for some reason, it does not work, please download the SQL dump from [here](http://soaresilva.eu/event_registration.sql) and import it.
5) Run `flask run` to start the development server.
6) Append `?event=a` or `?event=b` to the URL in order to see the two possible registration forms.