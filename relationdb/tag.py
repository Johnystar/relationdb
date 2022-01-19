"""
Tag utilities
"""

from .models import Tag
from typing import Union


def get_tags() -> list:
    return list(Tag.select())  # FIXME: sort by child tags


def get_tag_by_name(name: str) -> Union[Tag, None]:
    x = list(Tag.select().where(Tag.name == name))

    assert len(x) < 2

    if len(x) == 0:
        return None
    return x[0]


def get_tag_by_id(id: int) -> Union[Tag, None]:
    x = list(Tag.select().where(Tag.id == id))

    assert len(x) < 2

    if len(x) == 0:
        return None
    return x[0]
