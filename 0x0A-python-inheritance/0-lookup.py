#!/usr/bin/python3
def lookup(obj):
    attributes = []
    methods = []

    # Get the list of attributes
    for attr in dir(obj):
        if not callable(getattr(obj, attr)):
            attributes.append(attr)

    # Get the list of methods
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)

    # Return the combined list of attributes and methods
    return attributes + methods
