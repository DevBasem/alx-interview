#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def countLeadingSetBits(num):
    """Returns the number of leading set
    bits (1) in the given number."""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """Determines if a given data set represents
    a valid UTF-8 encoding."""
    remaining_bytes = 0
    for i in range(len(data)):
        if remaining_bytes == 0:
            remaining_bytes = countLeadingSetBits(data[i])
            # 1-byte (format: 0xxxxxxx)
            if remaining_bytes == 0:
                continue
            # A character in UTF-8 can be 1 to 4 bytes long
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            # Checks if current byte has format 10xxxxxx
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        remaining_bytes -= 1
    return remaining_bytes == 0
