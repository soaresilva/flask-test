from flask import Flask, render_template, flash, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, validators
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config')
mysql = MySQL(app)
csrf = CSRFProtect(app)


# Register form class
class RegisterForm(Form):
    name = StringField('Name', [validators.InputRequired(), validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.InputRequired(), validators.Length(min=6, max=50), validators.Email()])
    event = StringField('Event')


# Register
@app.route('/', methods=['GET', 'POST'])
def register():
    event = request.args.get('event', type=str)
    if event == 'a':
        event = 'Summer'
    elif event == 'b':
        event = 'Winter'
    else:
        return render_template('404.html')

    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data

        # Cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name, email, event) VALUES(%s, %s, %s)", (name, email, event))

        # Send to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Registration successful. Thank you.', 'success')

    return render_template('register.html', form=form, event=event)


if __name__ == '__main__':
    app.run(debug=True)