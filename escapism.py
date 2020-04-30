"""Escape strings to a safe set

Provide a generic API, given a set of safe characters and an escape character,
to escape safe strings and unescape the result.

A conservative default of [A-Za-z0-9] with _ as the escape character is used if
no args are provided.
"""

# Copyright (c) Min RK
# Distributed under the terms of the MIT License

import re
import string
import sys
import warnings

__version__ = "1.0.1"

SAFE = set(string.ascii_letters + string.digits)
ESCAPE_CHAR = '_'

if sys.version_info >= (3,):
    _ord = lambda byte: byte
    _bchr = lambda n: bytes([n])
else:
    _ord = ord
    _bchr = chr


def _escape_char(c, escape_char=ESCAPE_CHAR):
    """Escape a single character"""
    buf = []
    for byte in c.encode('utf8'):
        buf.append(escape_char)
        buf.append('%X' % _ord(byte))
    return ''.join(buf)


def escape(to_escape, safe=SAFE, escape_char=ESCAPE_CHAR, allow_collisions=False):
    """Escape a string so that it only contains characters in a safe set.

    Characters outside the safe list will be escaped with _%x_,
    where %x is the hex value of the character.

    If `allow_collisions` is True, occurrences of `escape_char`
    in the input will not be escaped.

    In this case, `unescape` cannot be used to reverse the transform
    because occurrences of the escape char in the resulting string are ambiguous.
    Only use this mode when:

    1. collisions cannot occur or do not matter, and
    2. unescape will never be called.

    .. versionadded: 1.0
        allow_collisions argument.
        Prior to 1.0, behavior was the same as allow_collisions=False (default).

    """
    if isinstance(to_escape, bytes):
        # always work on text
        to_escape = to_escape.decode('utf8')

    if not isinstance(safe, set):
        safe = set(safe)

    if allow_collisions:
        safe.add(escape_char)
    elif escape_char in safe:
        warnings.warn(
            "Escape character %r cannot be a safe character."
            " Set allow_collisions=True if you want to allow ambiguous escaped strings."
            % escape_char,
            RuntimeWarning,
            stacklevel=2,
        )
        safe.remove(escape_char)

    chars = []
    for c in to_escape:
        if c in safe:
            chars.append(c)
        else:
            chars.append(_escape_char(c, escape_char))
    return u''.join(chars)


def _unescape_char(m):
    """Unescape a single byte

    Used as a callback in pattern.subn. `m.group(1)` must be a single byte in hex,
    e.g. `a4` or `ff`.
    """
    return _bchr(int(m.group(1), 16))


def unescape(escaped, escape_char=ESCAPE_CHAR):
    """Unescape a string escaped with `escape`

    escape_char must be the same as that used in the call to escape.
    """
    if isinstance(escaped, bytes):
        # always work on text
        escaped = escaped.decode('utf8')
    
    escape_pat = re.compile(re.escape(escape_char).encode('utf8') + b'([a-z0-9]{2})', re.IGNORECASE)
    buf = escape_pat.subn(_unescape_char, escaped.encode('utf8'))[0]
    return buf.decode('utf8')
