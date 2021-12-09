import relationdb
from relationdb.models import initialise, Object, Tag, TagHiearchy
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


def test_basic_object_manipulation():
    # AUTOMATIC DELETION AND RE-INITIALISATION OF THE DATABASE #
    # FIXME: this is bad
    import os
    if os.path.exists('objects.db'):
        os.remove('objects.db')

    initialise()
    ############################################################

    example_ref = '/home/user/Documents/unorganised/file.txt'

    file = Object(refference=example_ref)
    file.save()

    tag_parents = [x.refference for x in relationdb.object.get_objects()]
    assert tag_parents == [example_ref]

    assert relationdb.object.get_object_by_refference(
        example_ref).refference == example_ref
