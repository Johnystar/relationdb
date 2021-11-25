"""
Defines database models
"""

from peewee import SqliteDatabase, Model, TextField, ForeignKeyField

db = SqliteDatabase("objects.db", pragmas={"foreign_keys": 1})


class BaseModel(Model):
    """
    (base database model)
    """

    class Meta:
        """
        (meta configuration for peewee)
        """

        database = db


class Object(BaseModel):
    """
    A tracked object
    """

    refference = TextField()


class Tag(BaseModel):
    """
    A tag that can be used to tag tracked objects
    """

    name = TextField()


# separate table, so that
# - parents can have multiple children
# - children can have multiple parents
class TagHiearchy(BaseModel):
    """
    Tag hiearchy defining relationships between tags
    """

    parent = ForeignKeyField(Tag, backref="child_tags")
    child = ForeignKeyField(Tag, backref="parent_tags")

    class Meta:
        indexes = ((("parent", "child"), True),)
