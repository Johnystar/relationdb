"""
Object utilities
"""

from .models import Object, Tag, ObjectTag
from typing import Union, Iterable
from .tag import get_tag_by_name
import peewee as pw


def get_objects() -> list[Object]:
    return list(Object().select())  # FIXME: sort by tags


def get_object_by_reference(reference: str) -> Union[Object, None]:
    x = list(Object.select().where(Object.reference == reference))

    assert len(x) < 2

    if len(x) == 0:
        return None
    return x[0]


def get_object_by_id(id: int) -> Union[Object, None]:
    x = list(Object.select().where(Object.id == id))

    assert len(x) < 2

    if len(x) == 0:
        return None
    return x[0]


def get_objects_by_tags(tags: Iterable[Union[str, Tag]]) -> list[Object]:
    processed_tags = []

    for tag in tags:
        if isinstance(tag, Tag):
            processed_tags.append(tag.id)
        elif isinstance(tag, str):
            x = get_tag_by_name(tag)
            if x is None:
                raise Exception('tag with name "{}" not found'.format(tag))
            processed_tags.append(x.id)
        else:
            raise Exception(
                'tag is neither str or Tag - shouldn\'t be possible')

    result = Object.select().join(ObjectTag).join(Tag).where(Tag.id.in_(
        processed_tags)).group_by(Object.reference).having(
            pw.fn.Count() == len(processed_tags))

    return list(result)
