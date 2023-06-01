from flask import Blueprint, render_template, request,  redirect, url_for
from .models import Event, Order

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    event = Event.query.all()  
    return render_template('index.html', events=event)

@bp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        search = '%' + request.args['search'] + '%'
        events = Event.query.filter(Event.event_description.like(search)).all()
        events_cat = Event.query.filter(Event.event_category.like(search)).all()
        if events or events_cat:
            return events
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))

@bp.route('/all')
def all():
    return redirect(url_for('main.index'))

@bp.route('/run')
def run():
    search = '%' + 'run' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)


@bp.route('/auction')
def auction():
    search = '%' + 'auction' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)

@bp.route('/donation')
def donation():
    search = '%' + 'donation' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)

@bp.route('/other')
def other():
    search = '%' + 'other' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)
    

@bp.route('/history')
def history():
    order = Order.query.all()  
    return render_template('history.html', orders=order)