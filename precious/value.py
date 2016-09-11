class ValueMeta(type):
    def __new__(meta, name, bases, namespace):
        if not namespace.get('_value_base'):
            assert 'attributes' in namespace, (
                '`Value` subclass has to define `attributes` iterable')

            namespace['__slots__'] = namespace['attributes']

        return super().__new__(meta, name, bases, namespace)


class Value(metaclass=ValueMeta):
    _value_base = True

    __slots__ = ()

    def values(self):
        return tuple(getattr(self, attr) for attr in self.attributes)

    def __repr__(self):
        return '{cls}({arguments})'.format(
            cls=self.__class__.__name__,
            arguments=', '.join(map(repr, self.values()))
        )

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return other.values() == self.values()

    def __hash__(self):
        return hash((self.__class__, ) + self.values())
