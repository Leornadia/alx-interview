#!/usr/bin/python3
"""
This module defines a function to determine if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the data to be validated.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """

    n_bytes = 0
    for i in range(len(data)):
        byte = data[i]

        # Check for a new UTF-8 character starting byte
        if n_bytes == 0:
            if (byte >> 7) == 0:  # Single byte character (0xxxxxxx)
                n_bytes = 0
            elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                n_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                n_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                n_bytes = 3
            else:
                return False  # Invalid starting byte
        else:
            # Check if the byte is a continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False  # Not a valid continuation byte
            n_bytes -= 1

    # Check if we reached the end of a valid character
    return n_bytes == 0
