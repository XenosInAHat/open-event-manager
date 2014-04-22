def index():
    events = db().select(db.event.ALL, orderby=db.event.title)
    return dict(events=events)

@auth.requires_login()
def create():
    form = SQLFORM(db.event).process(next=URL('index'))
    return dict(form=form)

def show():
    this_event = db.event(request.args(0,cast=int)) or redirect(URL('index'))
    this_event.update_record(author = auth.user_id)
    return dict(event=this_event)

def confirm():
    this_event = db.event(request.args(0,cast=int)) or redirect(
            URL('show', args=request.args(0,cast=int)))
    form = SQLFORM.confirm("Are you sure you'd like to delete this event?")
    if form.accepted:
        redirect(URL('delete', args=this_event.id))
    
    return dict(event=this_event, form=form)

def delete():
    db(db.event.id == request.args(0,cast=int)).delete()
    redirect(URL('index'))

def user():
    return dict(form=auth())
