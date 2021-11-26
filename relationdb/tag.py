"""
Tag utilities
"""

from .models import Tag


def get_tags():
    return Tag.select()  # FIXME: sort by child tags
