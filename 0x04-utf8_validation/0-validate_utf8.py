#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def validUTF8(data):
    # Function to check if a byte is valid as the start of a UTF-8 character
    def is_start_of_utf8(byte):
        return (byte >> 7) == 0b0 or (byte >> 6) == 0b10

    i = 0
    while i < len(data):
        # Determine number of bytes in current UTF-8 sequence
        if (data[i] >> 7) == 0b0:
            num_bytes = 1
        elif (data[i] >> 5) == 0b110:
            num_bytes = 2
        elif (data[i] >> 4) == 0b1110:
            num_bytes = 3
        elif (data[i] >> 3) == 0b11110:
            num_bytes = 4
        else:
            return False

        # Check that subsequent bytes (if any) start with 0b10
        for j in range(1, num_bytes):
            if i + j >= len(data) or not is_start_of_utf8(data[i + j]):
                return False

        i += num_bytes

    return True
