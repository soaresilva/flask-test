from flask import Flask, render_template, request, make_response, jsonify
from flask_mysqldb import MySQL
from wtforms import Form, StringField, validators, ValidationError
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config')
mysql = MySQL(app)
csrf = CSRFProtect(app)

options = {
    'a': 'Summer',
    'b': 'Winter'
}


# Register form class
class RegisterForm(Form):
    name = StringField('Name', [validators.InputRequired(), validators.Length(min=2, max=50)])
    email = StringField('Email', [validators.InputRequired(), validators.Length(min=6, max=50), validators.Email()])
    event = StringField('Event', [validators.InputRequired()])

    def validate_event(form, field):
        if field.data not in options:
            raise ValidationError("Invalid event")


# Register
@app.route('/', methods=['GET'])
def register():
    event = request.args.get('event', type=str)
    form = RegisterForm(request.form)
    if event in options:
        return render_template('register.html', event_label=options[event], event=event, form=form)
    else:
        return render_template('404.html')


@app.route('/', methods=['POST'])
def submit():
    try:
        form = RegisterForm(request.form)
        if form.validate():
            name = form.name.data
            email = form.email.data
            event = form.event.data
            # Cursor
            cur = mysql.connection.cursor()
            cur.execute('''USE event_registration''')
            cur.execute("INSERT INTO users(name, email, event) VALUES(%s, %s, %s)", (name, email, options[event]))
            # Send to DB
            mysql.connection.commit()
            # Close connection
            cur.close()

            message = 'Registration successful. Thank you.'
            status_code = 200
        else:
            message = form.errors
            status_code = 400
    except Exception as e:
        message = str(e)
        status_code = 500

    return make_response(jsonify(message=message), status_code)


if __name__ == '__main__':
    app.run(debug=True)
