from gluon.tools import *
db = DAL("sqlite://storage.sqlite")

auth = Auth(db)
auth.define_tables(username=True)
crud = Crud(db)

db.define_table('event',
        Field('title'),
        Field('event_date', 'date'),
        Field('host'),
        Field('location'),
        Field('description', 'text'),
        Field('public', 'boolean'),
        Field('author', default=session.auth.user if session.auth else None),
        format = '%(event)s')

db.define_table('guestlist',
        Field('name'),
        Field('email'),
        Field('phone', 'string'),
        format = '%(guestlist)s')

db.event.description.requires = IS_NOT_EMPTY()
db.event.event_date.requires = IS_NOT_EMPTY()
db.event.event_date.requires = IS_DATE()
db.event.host.requires = IS_NOT_EMPTY()
db.event.title.requires = IS_NOT_EMPTY()
db.event.author.readable = db.event.author.writable = False

db.guestlist.name.requires = IS_NOT_EMPTY()
db.guestlist.email.requires = IS_NOT_EMPTY()
db.guestlist.email.requires = IS_EMAIL()
