import mysql.connector
import config


# creates a new database event_registration
def create_db():
    try:
        connection = mysql.connector.connect(
            host=config.MYSQL_HOST, user=config.MYSQL_USER, password=config.MYSQL_PASSWORD
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE {};".format(config.MYSQL_DATABASE_DB))
    except mysql.connector.Error as error:
        raise error


# connects to newly created db to create a table 'users' with 5 columns: id, name, email, event, and registration date
def create_table():
    try:
        connection = mysql.connector.connect(
            host=config.MYSQL_HOST,
            database=config.MYSQL_DATABASE_DB,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
        )

        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE users (id int unsigned not null auto_increment, name varchar(50) not null, event varchar(
            50) not null, email varchar(50) not null, registration_date timestamp default current_timestamp, 
            primary key (id)); """
        )
    except mysql.connector.Error as error:
        raise error


if __name__ == "__main__":
    create_db()
    create_table()
