from gluon.tools import *
db = DAL("sqlite://storage.sqlite")

auth = Auth(db)
auth.define_tables(username=True)
crud = Crud(db)

db.define_table('event',
        Field('title'),
        Field('date'),
        Field('host'),
        Field('location'),
        Field('description', 'text'),
        format = '%(event)s')

db.event.description.requires = IS_NOT_EMPTY()
db.event.date.requires = IS_NOT_EMPTY()
db.event.host.requires = IS_NOT_EMPTY()
db.event.title.requires = IS_NOT_EMPTY()
