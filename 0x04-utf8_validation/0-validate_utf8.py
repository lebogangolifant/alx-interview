#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        - data: List of integers representing 1 byte of data each.
    Returns:
        - True if data is a valid UTF-8 encoding, else False.
    """

    nbytes = 0

    if not data or len(data) == 0:
        return True

    for num in data:
        bit = 1 << 7

        if nbytes == 0:
            while (bit & num):
                nbytes += 1
                bit >>= 1

            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (num & (1 << 7) and not (num & (1 << 6))):
                return False

        nbytes -= 1

    return nbytes == 0
