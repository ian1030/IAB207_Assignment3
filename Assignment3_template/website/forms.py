
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange
from .models import Event


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

class BookingForm(FlaskForm, Event):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    ticket_required = IntegerField("Ticket Neeeded", validators=[InputRequired("Enter a number"), NumberRange(min=1, max=Event.ticket_no, message="The input is invalid" )]) #the max can be the tcket number




