#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and len(str) >= n:
        first = str[:n]
        last = str[n+1:]
        return (first + last)
    return str
