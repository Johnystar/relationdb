from .models import Tag


def get_tags():
    return Tag.select()
