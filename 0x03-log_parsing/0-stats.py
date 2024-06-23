#!/usr/bin/python3
"""
Log parsing: read logs, compute stats, handle interruptions.
"""

import sys

if __name__ == '__main__':
    total_size = 0
    status_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    line_count = 0

    def print_stats(size: int, status_counts: dict) -> None:
        """
        Print file size and status code counts.
        """
        print(f"File size: {size}")
        for code in sorted(status_counts):
            if status_counts[code] > 0:
                print(f"{code}: {status_counts[code]}")

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                status_code = parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except IndexError:
                pass

            try:
                file_size = int(parts[-1])
                total_size += file_size
            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

        print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
