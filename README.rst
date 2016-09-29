Precious
========

.. image:: https://img.shields.io/pypi/v/precious.svg
    :target: https://pypi.python.org/pypi/precious
    :alt: Latest PyPI version

Value objects for Python


Example
-------

.. code-block:: python

   from precious import Value, assign_attributes


   class Color(Value):
       @assign_attributes
       def __init__(self, red, green, blue, alpha=0):
           pass


.. code-block:: python

   >>> red = Color(255, 0, 0)
   >>> red
   Color(255, 0, 0, 0)
   >>> red == Color(255, 0, 0)
   True
   >>> hash(red)
   8736776571231852889


Features
--------

- Memory efficient -- uses ``__slots__`` under the hood.
- Simple.
- Declarative syntax.


Installation
------------

.. code-block::

   pip install precious
