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

    # Number of consecutive 1s in the most significant bits
    num_consecutive_ones = 0

    # Iterate through each integer in the data
    for num in data:

        if num >= 128:
            # Count the number of consecutive 1s in the most significant bits
            mask = 128
            while (num & mask) != 0:
                num_consecutive_ones += 1
                mask >>= 1

            if num_consecutive_ones == 1 or num_consecutive_ones > 4:
                return False

            # Decrement the count for the first integer
            num_consecutive_ones -= 1

        elif (num & 128) != 0:
            return False

    return num_consecutive_ones == 0
