import pkg_resources

from precious.value import Value


__version__ = pkg_resources.require("precious")[0].version
__author__ = 'Marcin Biernat <mb@marcinbiernat.pl>'
__all__ = [
    'Value',
]
