import itertools
import inspect
from inspect import Parameter


def extract_attributes(__init__):
    if __init__.__name__ != '__init__':
        raise ValueError('Attributes can be extracted only from `__init__`')

    signature = inspect.signature(__init__)
    parameters = signature.parameters

    params_unpacked = (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD)

    for name, param in parameters.items():
        if param.kind in params_unpacked:
            raise TypeError('Extracing unpacked arguments is not supported')

    # Skip `self`
    extracted = tuple(itertools.islice(parameters.keys(), 1, None))

    __init__.value_attributes = extracted

    return __init__
