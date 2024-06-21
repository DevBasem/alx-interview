#!/usr/bin/python3
import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        if len(parts) < 7:
            continue
        
        try:
            size = int(parts[-1])
            status_code = int(parts[-2])
        except ValueError:
            continue
        
        total_size += size
        if status_code in status_codes:
            status_codes[status_code] += 1
        
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
