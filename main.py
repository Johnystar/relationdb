from peewee import *

db = SqliteDatabase('objects.db', pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db

class Object(BaseModel):
	refference = TextField()

class Tag(BaseModel):
	name = TextField()

# separate table, so that
# - parents can have multiple children
# - children can have multiple parents
class TagHiearchy(BaseModel):
	parent = ForeignKeyField(Tag, backref='child_tags')
	child = ForeignKeyField(Tag, backref='parent_tags')

	class Meta:
		indexes = (
			(('parent', 'child'), True),
		)