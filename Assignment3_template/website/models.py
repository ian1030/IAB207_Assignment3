from flask_login import UserMixin
from . import db
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(50), index=True, nullable=False)
    email_address = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)

    event = db.relationship('Event', backref='User')
    order = db.relationship('Order', backref='User')
    comment = db.relationship('Comment', backref='User')


class Event(db.Model):
    __tablename__ = 'events'
    

    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    event_name = db.Column(db.String(100), index=True, nullable=False)
    event_location = db.Column(db.String, nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    event_time = db.Column(db.Time, nullable=False)
    event_description = db.Column(db.String(250), nullable=False)
    event_category = db.Column(db.String(50), nullable=False)
    event_image = db.Column(db.String(50), nullable=False)
    event_ticket_quantity = db.Column(db.Integer, nullable=False)
    event_ticket_price = db.Column(db.Float, nullable=False)
    event_status = db.Column(db.String(50), nullable=False)

    user = db.relationship('User', backref='Event')


class Ticket(db.Model):
    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
    ticket_type = db.Column(db.String(50), nullable=False)

    event = db.relationship('Event', backref='Ticket')

class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, index=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.ticket_id'))
    date_ordered = db.Column(db.Date, nullable=False, default=datetime.now())
    number_of_tickets = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', backref='Order')
    ticket = db.relationship('Ticket', backref='Order')     

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
    comment = db.Column(db.Text, nullable=False)
    comment_date = db.Column(db.Date, default=datetime.now())

    user = db.relationship('User', backref='Comment')
    event = db.relationship('Event', backref='Comment') 