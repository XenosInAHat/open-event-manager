from gluon.tools import *
db = DAL("sqlite://storage.sqlite")

auth = Auth(db)
auth.define_tables(username=True)
crud = Crud(db)

db.define_table('event',
        Field('title'),
        Field('event_date', 'date'),
        #Field('date'),
        Field('host'),
        Field('location'),
        Field('description', 'text'),
        Field('public', 'boolean'),
        format = '%(event)s')

db.event.description.requires = IS_NOT_EMPTY()
db.event.event_date.requires = IS_NOT_EMPTY()
db.event.event_date.requires = IS_DATE()
db.event.host.requires = IS_NOT_EMPTY()
db.event.title.requires = IS_NOT_EMPTY()
