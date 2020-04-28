import mysql.connector
import config


def create_db():
    try:
        connection = mysql.connector.connect(
            host=config.MYSQL_HOST, user=config.MYSQL_USER, password=config.MYSQL_PASSWORD
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE {};".format(config.MYSQL_DATABASE_DB))
    except mysql.connector.Error as error:
        raise error


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
            """CREATE TABLE users (id int unsigned not null auto_increment, name varchar(50) not null, event varchar(50) not null, email varchar(50) not null, registration_date timestamp default current_timestamp, primary key (id)); """
        )
    except mysql.connector.Error as error:
        raise error


if __name__ == "__main__":
    create_db()
    create_table()
