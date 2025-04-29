from typing import Any

def compile(*args, **kwargs) -> Any:
    "Compile a regular expression pattern, returning a Pattern object."
    ...

def match(*args, **kwargs) -> Any:
    """Try to apply the pattern at the start of the string, returning
    a Match object, or None if no match was found."""
    ...

def search(*args, **kwargs) -> Any:
    """Scan through string looking for a match to the pattern, returning
    a Match object, or None if no match was found."""
    ...

def sub(*args, **kwargs) -> Any:
    """Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the Match object and must return
    a replacement string to be used."""
    ...
