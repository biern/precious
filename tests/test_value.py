import pytest

from precious import Value


class Point(Value):

    attributes = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


class LineSegment(Value):
    attributes = ('start', 'end')

    def __init__(self, start, end):
        self.start = start
        self.end = end


class TestValueInstances:
    @pytest.fixture
    def point_cls(self):
        return Point

    @pytest.fixture
    def line_cls(self):
        return LineSegment

    def test_initialized_attributes_values(self, point_cls):
        point = point_cls(1, 2)

        assert point.x == 1
        assert point.y == 2

    def test_repr(self, point_cls):
        assert repr(point_cls(0, 0)) == 'Point(0, 0)'

    def test_compound_repr(self, point_cls, line_cls):
        assert repr(line_cls(point_cls(0, 1), point_cls(2, 1))) == (
            'LineSegment(Point(0, 1), Point(2, 1))'
        )

    def test_objects_with_same_parameters_are_equal(self, point_cls):
        assert point_cls(0, 1) == point_cls(0, 1)

    def test_compound_objects_with_same_parameters_are_equal(
            self, point_cls, line_cls):

        assert (line_cls(point_cls(0, 1), point_cls(2, 1)) ==
                line_cls(point_cls(0, 1), point_cls(2, 1)))

    def test_objects_with_different_parameters_are_not_equal(self, point_cls):
        assert point_cls(0, 0) != point_cls(0, 1)

    def test_is_hashable(self, point_cls):
        hash(point_cls(0, 1))

    def test_uses_slots(self, point_cls):
        assert point_cls.__slots__ == ['x', 'y']

        with pytest.raises(AttributeError):
            point_cls(0, 0).foo = 'bar'
