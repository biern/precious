import pytest
from precious import Value


def test_attributes_are_required():
    with pytest.raises(AttributeError):
        class Foo(Value):
            def __init__(self):
                pass


def test_attributes_are_extracted_from_init():
    class Foo(Value):
        def __init__(self):
            pass
        __init__.value_attributes = ('x', 'y')

    assert Foo.attributes == ('x', 'y')
