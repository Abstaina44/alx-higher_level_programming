#!/usr/bin/python3

"""Module that formats, prints, and indents a text"""


def text_indentation(text):
    """Function that formats, prints, and indents a text
    Args:
        text (string): Text parameter to print

    Returns:
        Nothing
    """

    if not isinstance(text, (str)):
        raise TypeError("text must be a string")

    new_line = True

    for c in text:
        if new_line and c == ' ':
            continue

        new_line = False

        print(c, end='')

        if c in ".?:":
            print("\n")
            new_line = True
