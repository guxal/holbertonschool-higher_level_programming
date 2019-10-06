#!/usr/bin/python3
def text_indentation(text):
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    delim = ":.?"
    for x in delim:
        text = text.replace(x, "{}\n\n".format(x))
    text = text.replace('\\', '')
    text = "\n".join([line.strip() for line in text.split('\n')])
    print(text, end="")
