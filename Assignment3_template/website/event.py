from flask import Blueprint, flash, render_template, request, url_for, redirect
from .models import User, Event, Order
#import event  
from .forms import EventForm,CommentForm,BookingForm
from flask_login import current_user, login_required
from . import db
from datetime import datetime
import os 
from werkzeug.utils import secure_filename


#create blueprint 
eventbp = Blueprint('event',__name__,url_prefix='/events')



#show event 
@eventbp.route('/<int:event_id>')
def show(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if not event:
        flash('Event not found', 'error')
        return redirect(url_for('main.index'))
    # create the comment form
    cform = CommentForm()    
    return render_template('event/show.html', event=event, form=cform)

#Create Event 
@eventbp.route('/create',methods=['GET','POST'])
@login_required
def create_event():
    create = EventForm()
    if (create.validate_on_submit() == True):

        db_file_path = check_upload_file(create)
        eventstatus = 'Open'
    
        new_event = Event(event_name=create.event_name.data,
                          event_location=create.event_location.data,
                          event_date = create.event_date.data,
                          event_time = create.event_time.data,
                          event_description = create.event_description.data,
                          event_category = create.event_category.data,
                          event_image = db_file_path,
                          event_ticket_quantity = create.event_ticket_quantity.data,
                          event_ticket_price = create.event_ticket_price.data,
                          event_status = eventstatus,
                          user = current_user)
        
        db.session.add(new_event)
        db.session.commit()

        flash('Event created successfully!','success')
        return redirect(url_for('event.create_event'))
    return render_template('event/create.html',form=create)

def check_upload_file(form):
    #get file data from form  
    fp=form.image.data
    filename=fp.filename
    #get the current path of the module file… store image file relative to this path  
    BASE_PATH=os.path.dirname(__file__)
    # upload file location – directory of this file/static/image
    upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
    #store relative path in DB as image location in HTML is relative
    db_upload_path='/static/image/' + secure_filename(filename)
    #save the file and return the db upload path  
    fp.save(upload_path)
    return db_upload_path

#Update Event 
@eventbp.route('/<int:event_id>/update', methods=['GET', 'POST'])
@login_required
def update(event_id):
    event = Event.query.get(event_id)
    if not event:
        flash('Event not found', 'error')
        return redirect(url_for('main.index'))

    if event.user != current_user:
        flash('You do not have permission to update this event', 'error')
        return redirect(url_for('event.show', event_id=event.id))

    update = EventForm(obj=event)
    if update.validate_on_submit():
        event.eventname = update.event_name.data
        event.eventlocation = update.event_location.data
        event.eventdate = update.event_date.data
        event.eventtime = update.event_time.data
        event.description = update.event_description.data
        event.category = update.event_category.data
        event.image = update.event_image.data 
        event.ticket = update.event_ticket_quantity.data
        event.price = update.event_ticket_price.data 

        db.session.commit()

        flash('Event updated successfully!', 'success')
        return redirect(url_for('event.show', event_id=event.id))

    return render_template('event/update.html', form=update, event=event)

#Cancel Event
@eventbp.route('/<int:event_id>/cancel', methods=['POST'])
@login_required
def cancel(event_id):
    event = Event.query.get(event_id)
    if not event:
        flash('Event not found', 'error')
        return redirect(url_for('main.index'))

    if event.user != current_user:
        flash('You do not have permission to cancel this event', 'error')
        return redirect(url_for('event.show', event_id=event.id))

    event.event_status = 'Cancelled'
    db.session.commit()

    flash('Event cancelled successfully!', 'success')
    return redirect(url_for('event.show', event_id=event.id))


#Booking Event Ticket
@eventbp.route('/<event>/booking', methods = ['GET', 'POST'])
@login_required
def booking(event):
  event_obj = Event.query.filter_by(id=event).first()
  ticket_obj = Event.query.filter_by(id=event).first()
  print('Method type: ', request.method)
  form = BookingForm()
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

