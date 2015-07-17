# coding: utf-8
from escapism import escape, unescape

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

    