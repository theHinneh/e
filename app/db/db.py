from databases import Database
from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, UniqueConstraint, Index)

DATABASE_URL = 'postgresql://postgres:postgres@localhost/elections_platform'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

elections_platform = Table(
    'elections',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('org_name', String(56)),
    Column('telephone', String(15)),
    Column('email', String(56)),
    Column('country', String(56)),

    UniqueConstraint('email', 'telephone')
)
Index('unique', elections_platform.c.email, elections_platform.c.telephone, unique=True)
database = Database(DATABASE_URL)

