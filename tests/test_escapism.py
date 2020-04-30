# coding: utf-8

import warnings

import pytest

from escapism import escape, unescape, SAFE

text = type(u'')

test_strings = [
    u'asdf',
    u'sposmål',
    u'godtbrød',
    u'≠¡™£¢∞§¶¨•d',
    u'_\\-+',
]


def test_escape_default():
    for s in test_strings:
        e = escape(s)
        assert isinstance(e, text)
        u = unescape(e)
        assert isinstance(u, text)
        assert u == s


def test_escape_custom_char():
    for escape_char in r'\-%+_':
        for s in test_strings:
            e = escape(s, escape_char=escape_char)
            assert isinstance(e, text)
            u = unescape(e, escape_char=escape_char)
            assert isinstance(u, text)
            assert u == s


def test_escape_custom_safe():
    safe = 'ABCDEFabcdef0123456789'
    escape_char = '\\'
    safe_set = set(safe + '\\')
    for s in test_strings:
        e = escape(s, safe=safe, escape_char=escape_char)
        assert all(c in safe_set for c in e)
        u = unescape(e, escape_char=escape_char)
        assert u == s


def test_safe_escape_char():
    escape_char = "-"
    safe = SAFE.union({escape_char})
    with pytest.warns(RuntimeWarning):
        e = escape(escape_char, safe=safe, escape_char=escape_char)
    assert e == "{}{:02X}".format(escape_char, ord(escape_char))
    u = unescape(e, escape_char=escape_char)
    assert u == escape_char


def test_allow_collisions():
    escaped = escape('foo-bar ', escape_char='-', allow_collisions=True)
    assert escaped == 'foo-bar-20'
