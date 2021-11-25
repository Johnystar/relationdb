"""
Defines the base model for all database models
"""

from peewee import SqliteDatabase, Model

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
