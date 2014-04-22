def index():
    events = db().select(db.event.ALL, orderby=db.event.title)
    return dict(events=events)

@auth.requires_login()
def create():
    form = SQLFORM(db.event).process(next=URL('index'))
    return dict(form=form)

def show():
    this_event = db.event(request.args(0,cast=int)) or redirect(URL('index'))
    return dict(event=this_event)

def user():
    return dict(form=auth())
