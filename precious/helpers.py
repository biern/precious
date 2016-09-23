import itertools
import inspect
from inspect import Parameter
import functools


def extract_attributes(__init__):
    if __init__.__name__ != '__init__':
        raise ValueError('Attributes can be extracted only from `__init__`')

    signature = inspect.signature(__init__)
    parameters = signature.parameters

    params_unpacked = (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD)

    for name, param in parameters.items():
        if param.kind in params_unpacked:
            raise TypeError('Extracing unpacked arguments is not supported')

    # Skips `self`
    extracted = tuple(itertools.islice(parameters.keys(), 1, None))

    __init__.value_attributes = extracted

    return __init__


def assign_attributes(__init__):
    __init__ = extract_attributes(__init__)

    defaults = {
        name: param.default for name, param in
        inspect.signature(__init__).parameters.items()
        if param.default != Parameter.empty
    }

    @functools.wraps(__init__)
    def assign(self, *args, **kwargs):
        arguments = _get_arguments(self.attributes, args, kwargs, defaults)

        for attr, value in arguments.items():
            setattr(self, attr, value)

        __init__(self, *args, **kwargs)

    return assign


def _get_arguments(attributes, args, kwargs, defaults):
    positional = attributes[:len(args)]
    keywords = attributes[len(args):]

    arguments = {attr: args[i] for i, attr in enumerate(positional)}

    for attr in keywords:
        try:
            arguments[attr] = kwargs[attr]
        except KeyError:
            try:
                arguments[attr] = defaults[attr]
            except KeyError:
                raise TypeError(
                    "missing required argument: '{}'".format(attr))

    return arguments
