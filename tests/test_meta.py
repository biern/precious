import pytest
from precious import Value


class TestMeta:
    def test_attributes_are_required(self):
        with pytest.raises(AttributeError):
            class Foo(Value):
                def __init__(self):
                    pass

    def test_attributes_are_extracted_from_init(self):
        class Foo(Value):
            def __init__(self):
                pass
            __init__.value_attributes = ('x', 'y')

        assert Foo.attributes == ('x', 'y')

    def test_sets_slots(self):
        class Foo(Value):
            attributes = ('foo', )

        assert Foo.__slots__ == ('foo', )
