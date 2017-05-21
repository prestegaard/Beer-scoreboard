from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('nickname', VARCHAR(length=64)),
    Column('button_color', VARCHAR(length=64)),
    Column('about_me', VARCHAR(length=140)),
    Column('img_src', VARCHAR(length=64)),
    Column('last_seen', VARCHAR(length=64)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('nickname', String(length=64)),
    Column('button_color', String(length=64)),
    Column('about_me', String(length=140)),
    Column('img_src', String(length=64)),
    Column('location', String(length=140)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['last_seen'].drop()
    post_meta.tables['user'].columns['location'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['last_seen'].create()
    post_meta.tables['user'].columns['location'].drop()
