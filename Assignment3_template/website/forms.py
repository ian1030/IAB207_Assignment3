from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, IntegerField, SelectField, DateField, TimeField, FileField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange
from .models import Event
from flask_wtf.file import FileRequired, FileAllowed

Allowed_File = {'PNG', 'JPG', 'png', 'jpg', 'JPEG', 'jpeg'}

# User Login Form 
class LoginForm(FlaskForm):
    username = StringField("User Name:", validators=[InputRequired('Enter User Name')])   
    password = PasswordField("Password:", validators=[InputRequired('Enter a Password')])      
    submit = SubmitField("Login")

# User Register Form
class RegisterForm(FlaskForm):
    name = StringField("User Name:", validators=[InputRequired()])
    email = StringField("Email:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired(), Length(min=6, message="Password must exceed 6 words"), EqualTo('confirm', message="Password didn't match")])
    confirm = PasswordField("Confirm Password:")
    phone = IntegerField("Phone Number:", validators=[InputRequired()])
    address = TextAreaField("Address:", validators=[InputRequired()])
    submit = SubmitField("Register")

# Comment Form 
class CommentForm(FlaskForm):
    text = TextAreaField("Comment:", validators=[InputRequired(), Length(min=3, max=400, message="Comment can't exceed 400 words and must be more than 3 words")])
    submit = SubmitField("Post")

# Booking Form 
class BookingForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    ticket_required = IntegerField("Ticket Needed", validators=[InputRequired("Enter a number"), NumberRange(min=1, max=9999, message="The input is invalid")])
    submit = SubmitField("Book")

# Create New Event 
class EventForm(FlaskForm):
    event_name = StringField("Event Name:", validators=[InputRequired()])
    event_location = StringField("Location:", validators=[InputRequired()])
    event_date = DateField("Date:", validators=[InputRequired()])
    event_time = TimeField("Time:", validators=[InputRequired()])
    event_description = TextAreaField("Description:", validators=[InputRequired()])
    event_category = SelectField("Category:", choices=[
        ('Charity Run', 'Charity Run'),
        ('Charity Action', 'Charity Action'),
        ('Charity Food Donation', 'Charity Food Donation'),
        ('Others', 'Others')
    ], validators=[InputRequired()])
    image = FileField('Event Image', validators=[
        FileRequired(message='Image cannot be empty'),
        FileAllowed(Allowed_File, message='Only supports PNG, JPG, JPEG')
    ])
    event_ticket_quantity = IntegerField('Ticket Quantity:', validators=[InputRequired(), NumberRange(min=1)])
    event_ticket_price = IntegerField('Ticket Price:', validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField("Create")

class UpdateEventForm(FlaskForm):
    event_name = StringField("Event Name:", validators=[InputRequired()])
    event_location = StringField("Location:", validators=[InputRequired()])
    event_date = DateField("Date:", validators=[InputRequired()])
    event_time = TimeField("Time:", validators=[InputRequired()])
    event_description = TextAreaField("Description:", validators=[InputRequired()])
    event_category = SelectField("Category:", choices=[
        ('Charity Run', 'Charity Run'),
        ('Charity Action', 'Charity Action'),
        ('Charity Food Donation', 'Charity Food Donation'),
        ('Others', 'Others')
    ], validators=[InputRequired()])
    image = FileField('Event Image', validators=[
        FileRequired(message='Image cannot be empty'),
        FileAllowed(Allowed_File, message='Only supports PNG, JPG, JPEG')
    ])
    event_ticket_quantity = IntegerField('Ticket Quantity:', validators=[InputRequired(), NumberRange(min=1)])
    event_ticket_price = IntegerField('Ticket Price:', validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField("Update")
