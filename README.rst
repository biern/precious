Precious
========

.. image:: https://img.shields.io/pypi/pyversions/precious.svg
    :target: https://pypi.python.org/pypi/precious
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/biern/precious.svg?branch=master
    :target: https://travis-ci.org/biern/precious
    :alt: Latest Travis CI build status

Value objects for Python.


Example
-------

.. code-block:: python

   from precious import Value, assign_attributes


   class Color(Value):
       @assign_attributes
       def __init__(self, red, green, blue, alpha=0): pass

       @property
       def grayscale(self):
           return (self.r + self.g + self.b) / 3


.. code-block:: python

   >>> red = Color(255, 0, 0)
   >>> red
   Color(255, 0, 0, 0)
   >>> red == Color(255, 0, 0)
   True
   >>> Color.__slots__
   ('red', 'green', 'blue', 'alpha')
   >>> hash(red)
   8736776571231852889


Installation
------------

.. code-block::

   pip install precious


Usage
-----

Value object classes should subclass base ``Value`` class. Every ``Value`` subclass has to define ``attributes``, which is an iterable containing names of all attributes.
This may happen by explicitly setting the attribute on the class:

.. code-block:: python

   class Point(Value):
       attributes = ('x', 'y')

       def __init__(self, x, y):
           self.x = x
           self.y = y


By extracting attribute names directly from ``__init__`` definition using one of provided helper decorators:

.. code-block:: python

   from precious import Value, extract_attributes

   class Point(Value):
       @extract_attributes
       def __init__(self, x, y):
           self.x = x
           self.y = y


By using a shortcut ``assign_attributes`` to replace a common boilerplate of extracting and assigning all the attributes in ``__init__``:

.. code-block:: python

   from precious import Value, assign_attributes

   class Point(Value):
       @assign_attributes
       def __init__(self, x, y): pass


Note that in the example above attributes are not being assigned in parent's class ``__init__``, thus no ``super()`` call is required.


Features
--------

``Value`` implements
********************

* ``__eq__``
* ``__repr__``
* ``__hash__``


Memory efficiency
*****************

Subclassing ``Value`` automaticaly assignes names of all attributes to ``__slots__`` [1]_.

Testing
-------

Just run ``tox`` in package directory:

.. code-block:: bash

  $ tox


Why not simply use ``namedtuple``?
----------------------------------

Namedtuple definition is equally fine for simple use cases.

.. code-block:: python

    Point = namedtuple('Point', ('x', 'y'))


Having to repeat the classname is a minor inconvinience, but the definition is pretty readable and concise. Also, class gets iterable interface and indexing support, which sometimes is what you want. However, things with namedtuple get very ugly when a default value or a method or a property is required. Subclassing is the only way to go. Consider the following example:

.. code-block:: python

    class Color(namedtuple('Color_', ('r', 'g', 'b', 'alpha'))):
        __slots__ = ()

        def __new__(cls, r, g, b, alpha=0):
            return super().__new__(cls, r, g, b, alpha)

        @property
        def grayscale(self):
            return (self.r + self.g + self.b) / 3

    # Equivalent to

    class Color(Value):
        @assign_attributes
        def __init__(self, red, green, blue, alpha=0): pass

        @property
        def grayscale(self):
            return (self.r + self.g + self.b) / 3


To sum up, problems with extending namedtuple include:

* Having to define empty ``__slots__`` [1]_.
* Overriding ``__new__`` when a default values is required.
* Repeating attributes names in several places.
* Unintuitive inheritance by generating parent class on the fly.


.. [1] https://docs.python.org/3/reference/datamodel.html#slots
