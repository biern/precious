from precious import Value, assign_attributes, copy


class Point(Value):
    @assign_attributes
    def __init__(self, x, y): pass


class TestCopyObject:
    def test_copy_object_with_same_attributes(self):
        p1 = Point(1, 2)
        p2 = copy(p1)

        assert p2.x == 1
        assert p2.y == 2

    def test_copy_object_with_changed_attribute(self):
        p1 = Point(1, 2)
        p2 = copy(p1, x=3)

        assert p2.x == 3
        assert p2.y == 2
