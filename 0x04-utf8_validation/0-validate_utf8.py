#!/usr/bin/python3
"""
UTF-8 Validation Module
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    
    :param data: List of integers, where each integer represents a byte
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    num_bytes = 0

    # Masks to check the first few bits of a byte
    first_byte_mask_1 = 1 << 7  # 10000000
    first_byte_mask_2 = 1 << 6  # 01000000

    for num in data:
        # Extract the 8 least significant bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # If no leading 1's, it is a single byte character (ASCII)
            if num_bytes == 0:
                continue

            # UTF-8 characters can only be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Check that the current byte is of the form 10xxxxxx
            if not (byte & first_byte_mask_1 and not (byte & first_byte_mask_2)):
                return False

        num_bytes -= 1

    # If num_bytes is not zero, it means we were expecting more continuation bytes
    return num_bytes == 0

# Example usage:
if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # Should return True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # Should return True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # Should return False

