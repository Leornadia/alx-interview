#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: A list of integers where each integer represents 1 byte of data
    :return: True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit (8th bit from the left) is set to 1
    mask1 = 1 << 7
    # Mask to check if the second most significant bit is set to 1
    mask2 = 1 << 6

    for num in data:
        # Check only the 8 least significant bits of each integer
        byte = num & 255

        if n_bytes == 0:
            # Determine how many bytes the UTF-8 character has
            mask = mask1
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1
            
            # 1-byte character
            if n_bytes == 0:
                continue
            
            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte starts with 10
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        n_bytes -= 1

    # All bytes have been processed
    return n_bytes == 0


if __name__ == "__main__":
    # Test cases can be added here
    pass
