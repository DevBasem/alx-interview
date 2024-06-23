#!/usr/bin/python3
"""
This script reads log data from stdin, computes metrics, and
prints statistics including total file size and counts of
each status code.
"""
import sys
import signal

def print_stats(total_size, status_counts):
    """
    Print current statistics including total file size
    and counts of each status code.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def parse_line(line):
    """
    Parse each line of log input to extract IP, status code,
    and file size. Returns None for invalid lines.
    """
    try:
        parts = line.split()
        ip = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip, status_code, file_size
    except Exception:
        return None, None, None

def main():
    """
    Main function to process log input from stdin,
    compute metrics, and print statistics.
    """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0
    
    signal.signal(signal.SIGINT, lambda signal, frame: print_stats(total_size, status_counts) or sys.exit(0))
    
    for line in sys.stdin:
        line_count += 1
        ip, status_code, file_size = parse_line(line.strip())
        
        if ip is None or status_code not in status_counts:
            continue
        
        total_size += file_size
        status_counts[status_code] += 1
        
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
