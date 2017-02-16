# Escapism

Simple escaping of text, given a set of safe characters and an escape character.

## Usage

Not much to it. Two functions:

```python
escaped = escapism.escape('string to escape')
# 'string_20to_20escape'
original = escapism.unescape(escaped)
```

There are two optional arguments you can pass to `escape()`:

- `safe`: a string or set of characters that don't need escaping. Default: ascii letters and numbers.
- `escape_char`: a single character used for escaping. Default: `_`.
  `escape_char` will never be considered a safe value.

`unescape()` accepts the same `escape_char` argument as `escape()` if a value other than the default is used.

```python
import string
import escapism
safe = string.ascii_letters + string.digits + '@_-.+'
escape_char = r'%'
escaped = escapism.escape('foø-bar@%!xX?', safe=safe, escape_char=escape_char)
# 'fo%C3%B8-bar@%25%21xX%3F'
original = escapism.unescape(escaped, escape_char=escape_char)
```
