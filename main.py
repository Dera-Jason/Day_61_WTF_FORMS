from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os

load_dotenv()

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min= 8, max= 30, message="Field must be at least 8 characters long.")])
    submit = SubmitField('Log In')

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
bootstrap  = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
