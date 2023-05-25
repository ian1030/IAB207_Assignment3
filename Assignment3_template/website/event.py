from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Order
from .forms import CommentForm, BookingForm
from . import db, app
import os
from werkzeug.utils import secure_filename
#additional import:
from flask_login import login_required, current_user

eventbp = Blueprint('event', __name__, url_prefix='/events')


@eventbp.route('/<id>')
def show(id):
    event = Event.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()    
    return render_template('event/show.html', event=event, form=cform)


@eventbp.route('/<event>/booking', methods = ['GET', 'POST'])
#@login_required
def booking(event):
  event_obj = Event.query.filter_by(id=event).first()
  ticket_obj = Event.query.filter_by(id=event).first()
  print('Method type: ', request.method)
  form = BookingForm(event_obj)
  if form.validate_on_submit():
    ticket_no=form.ticket_required.data
    if ticket_no > ticket_obj.event_ticket_quantity:
       flash('Invalid ticket number insert', 'failed')
       return redirect(url_for('event.show'))
    else:
      if event_obj.event_ticket_quantity == ticket_no:
        event_obj.event_ticket_quantity = 0
        event_obj.event_status = 'Sold Out'
      else:
        event_obj.event_ticket_quantity = event_obj.event_ticket_quantity - ticket_no
      booking = Order(
                    ticket_no=form.ticket_required.data,  
                    ticket = ticket_obj,
                    event = event_obj,
                    user= current_user,
                    number_of_tickets = ticket_no,
                      )
      # commit to the database
      db.session.add(booking) 
      db.session.commit()
      flash('Successfully booked', 'success')
      #Always end with redirect when form is valid
      return redirect(url_for('event.show'))
  return render_template('destinations/create.html', form=form)
