"""
Initialises a new database
"""

from relationdb.models import Object, Tag, TagHiearchy, db

db.create_tables((Object, Tag, TagHiearchy))
