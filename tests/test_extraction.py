import pytest
from contextlib import contextmanager

from precious import Value, extract_attributes


class Point(Value):
    @extract_attributes
    def __init__(self, x, *, y, z='foo'):
        self.x = x
        self.y = y
        self.z = z


class TestExtractionIntegration:
    def test_attributes_are_assigned(self):
        assert Point.attributes == ('x', 'y', 'z')


class TestExtraction:
    @contextmanager
    def assert_extraction_unpacking_error(self):
        with pytest.raises(
                TypeError,
                message="Extracing unpacked arguments is not supported"):
            yield

    def test_positional_arguments(self):
        @extract_attributes
        def __init__(self, x, y):
            pass

        assert __init__.value_attributes == ('x', 'y')

    def test_keyword_only_arguments(self):
        @extract_attributes
        def __init__(self, *, x, y):
            pass

        assert __init__.value_attributes == ('x', 'y')

    def test_keyword_with_default_value(self):
        @extract_attributes
        def __init__(self, x='foo'):
            pass

        assert __init__.value_attributes == ('x', )

    def test_args_are_not_allowed(self):
        with self.assert_extraction_unpacking_error():
            @extract_attributes
            def __init__(self, x, y, *args):
                pass

    def test_kwargs_are_not_allowed(self):
        with self.assert_extraction_unpacking_error():
            @extract_attributes
            def __init__(self, x, y, **kwargs):
                pass

    def test_raises_error_if_not_used_with_init(self):
        with pytest.raises(
                ValueError,
                message='Only __init__ can be decorated'):
            @extract_attributes
            def foo(self, x):
                pass
