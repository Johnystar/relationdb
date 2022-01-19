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

    file = Object(reference=example_ref)
    file.save()

    tag_parents = [x.reference for x in relationdb.object.get_objects()]
    assert tag_parents == [example_ref]

    assert relationdb.object.get_object_by_reference(
        example_ref).reference == example_ref


def test_core_find_object_by_tag():
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

    example_ref = '/home/user/Videos/unorganised/file.mkv'

    file = Object(reference=example_ref)
    file.save()
    file.add_tag(video_tag)

    assert relationdb.object.get_objects_by_tags(
        [video_tag])[0].reference == file.reference
    assert relationdb.object.get_objects_by_tags([video_tag])[0] == file
