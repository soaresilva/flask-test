from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, validators

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = '3306'
app.config['MYSQL_UNIX_SOCKET'] = '/Applications/mampstack-7.3.13-0/mysql/tmp/mysql.sock'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootroot'
app.config['MYSQL_DB'] = 'flask_event_reg'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("welcome.html")


# Register form class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    event = StringField('Event', [validators.Length(min=4, max=25)])


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        event = form.event.data

        # Cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name, email, event) VALUES(%s, %s, %s)", (name, email, event))

        # Send to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Thanks for your registration.', 'success')

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.secret_key('secret123')
    app.run(debug=True)