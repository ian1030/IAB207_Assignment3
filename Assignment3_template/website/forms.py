
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange
from .models import Event


# User Login Form 
class LoginForm(FlaskForm):
    username=StringField("User Name:", validators=[InputRequired('Enter User Name')])   
    password=PasswordField("Password:", validators=[InputRequired('Enter a Password')])      
    submit = SubmitField("Login")

# User Register Form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name: ", validators=[InputRequired()])
    password=PasswordField("Password: ", validators=[InputRequired(),Length(min=6,message="Password must exceed 6 words"),EqualTo('confirm', message="Password didnt match")])
    confirm = PasswordField("Confirm Password:")
    email = StringField("Email: ", validators=[InputRequired()])
    phone = IntegerField("Phone Number: ", validators=[InputRequired()])
    submit = SubmitField("Register")

# Comment Form 
class CommentForm(FlaskForm):
    commenttext = TextAreaField("Comment: ", validators=[InputRequired(),Length(min=3, max=400, message="Comment Can't exceed 400 words and must more than 3 words")])
    submit = SubmitField("Post")

# Booking Form 
class BookingForm(FlaskForm, Event):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    ticket_required = IntegerField("Ticket Neeeded", validators=[InputRequired("Enter a number"), NumberRange(min=1, max=Event.ticket_no, message="The input is invalid" )]) #the max can be the tcket number




