"""
Defines database models
"""

from peewee import TextField, ForeignKeyField
from .base_model import db, BaseModel


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


def initialise():
    db.create_tables((Object, Tag, TagHiearchy))
