"""
Object utilities
"""

from .models import Object, Tag
from typing import Union, Sequence
from .tag import get_tag_by_name


def get_objects() -> list[Object]:
    return list(Object().select())  # FIXME: sort by tags


def get_object_by_refference(refference: str) -> Union[Object, None]:
    x = list(Object.select().where(Object.refference == refference))

    assert len(x) < 2

    if len(x) == 0:
        return None
    return x[0]


def get_objects_by_tags(tags: Sequence[Union[str, Tag]]) -> list[Object]:
    processed_tags = []

    for tag in tags:
        if tag is Tag:
            processed_tags.append(tag.id)
        elif tag is str:
            x = get_tag_by_name(tag)
            if x is None:
                raise Exception('tag with name "{}" not found'.format(tag))
            processed_tags.append(x.id)
        else:
            raise Exception(
                'tag is neither str or Tag - shouldn\'t be possible')

    tag_selection = Tag.select(Tag.id).where(Tag.id in processed_tags)
    # return list(Object.select().where(Object.))
    # https://stackoverflow.com/a/44378685
    # ?
