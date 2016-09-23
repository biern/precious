from precious import Value, assign_attributes


class Color(Value):
    @assign_attributes
    def __init__(self, red, green, blue, *, opacity=1):
        pass


class TestAssignmentIntegration:
    def test_attributes_are_assigned(self):
        yellow = Color(0, 1, 1)
        assert yellow.red == 0
        assert yellow.green == 1
        assert yellow.blue == 1
        assert yellow.opacity == 1, 'default value has not been assigned'

    def test_override_default_attribute(self):
        yellow = Color(0, 1, 1, opacity=0)
        assert yellow.red == 0
        assert yellow.green == 1
        assert yellow.blue == 1
        assert yellow.opacity == 0


class TestAssignAttributes:
    def test_extracts_attributes(self, mocker):
        def foo(self, a, b):
            pass

        mock_extract = mocker.patch(
            'precious.helpers.extract_attributes',
            autospec=True,
            return_value=foo,
        )
        foo.value_attributes = ('a', 'b')

        foo = assign_attributes(foo)

        assert foo.value_attributes == ('a', 'b')
        assert mock_extract.call_count == 1
