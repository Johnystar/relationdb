import relationdb
from relationdb.models import initialise, Tag, TagHiearchy
from relationdb import __version__

import toml


def test_version():
    assert __version__ == toml.load('pyproject.toml')[
        'tool']['poetry']['version']


def test_basic_tag_manipulation():
    # AUTOMATIC DELETION AND RE-INITIALISATION OF THE DATABASE #
    # FIXME: this is bad
    import os
    if os.path.exists('objects.db'):
        os.remove('objects.db')

    initialise()
    ############################################################

    video_tag = Tag(name='video')
    video_tag.save()

    media_tag = Tag(name='media')
    media_tag.save()

    TagHiearchy(parent=media_tag, child=video_tag).save()

    tag_parents = [(x.name, len(list(x.parent_tags)))
                   for x in relationdb.tag.get_tags()]
    assert tag_parents == [('video', 1), ('media', 0)]
