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

__version__ = '0.0.1'

SAFE = set(string.ascii_letters + string.digits)
ESCAPE_CHAR = '_'


def _escape_char(c, escape_char=ESCAPE_CHAR):
    """Escape a single character"""
    buf = []
    for byte in c.encode('utf8'):
        buf.append(escape_char)
        buf.append('%X' % byte)
    return ''.join(buf)


def escape(to_escape, safe=SAFE, escape_char=ESCAPE_CHAR):
    """Escape a string so that it only contains characters in a safe set.
    
    Characters outside the safe list will be escaped with _%x_,
    where %x is the hex value of the character.
    """
    if isinstance(to_escape, bytes):
        # always work on text
        to_escape = to_escape.decode('utf8')
    
    if not isinstance(safe, set):
        safe = set(safe)
    if escape_char in safe:
        # escape char can't be in safe list
        safe.remove(escape_char)
    
    chars = []
    for c in to_escape:
        if c in safe:
            chars.append(c)
        else:
            chars.append(_escape_char(c, escape_char))
    return ''.join(chars)


def _unescape_char(m):
    """Unescape a single byte
    
    Used as a callback in pattern.subn. `m.group(1)` must be a single byte in hex,
    e.g. `a4` or `ff`.
    """
    return bytes([int(m.group(1), 16)])


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
