from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Destination, Event
from .forms import DestinationForm, CommentForm, BookingForm
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
  print('Method type: ', request.method)
  form = BookingForm(event_obj)
  if form.validate_on_submit():
    ticket_no=form.ticket_required.data
    event_obj.ticket_no = event.ticket_no - ticket_no
    booking = Event(
                  ticket_no=form.ticket_required.data,  
                  event=event_obj,
                  user=current_user,
                )
    # commit to the database
    db.session.add(booking) 
    db.session.commit()
    flash('Successfully booked', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('event.show'))
  return render_template('destinations/create.html', form=form)
