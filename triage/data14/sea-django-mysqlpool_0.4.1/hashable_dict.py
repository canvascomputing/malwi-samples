class HashableDict(dict):
    """A dictionary that is hashable.

    This is not generally useful, but created specifically to hold the ``conv``
    parameter that needs to be passed to MySQLdb.
    """

    def __hash__(self):
        """Calculate the hash of this ``dict``.

        The hash is determined by converting to a sorted tuple of key-value
        pairs and hashing that.
        """
        items = [(n, tuple(v)) for n, v in self.items() if isiterable(v)]
        return hash(tuple(items))


def isiterable(value):
    """Determine whether ``value`` is iterable."""
    try:
        iter(value)
        return True
    except TypeError:
        return False
