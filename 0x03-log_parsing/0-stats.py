#!/usr/bin/python3
import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
    sys.stdout.flush()

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Register signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        
        if len(parts) >= 7:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                
                total_file_size += file_size
                
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                
                line_count += 1
                
                if line_count % 10 == 0:
                    print_statistics()
            
            except ValueError:
                # If status code or file size cannot be converted to int, skip the line
                continue

except KeyboardInterrupt:
    pass

print_statistics()
