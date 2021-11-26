"""
Object utilities
"""

from .models import Object


def get_objects():
    return Object().select()  # FIXME: sort by tags
