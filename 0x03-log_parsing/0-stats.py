#!/usr/bin/python3

import sys
import signal
import re

# Initialize global variables
total_size = 0
status_codes = {}
line_count = 0

# Define the valid status codes
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

def print_stats():
    """Print the statistics collected so far."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption."""
    print_stats()
    sys.exit(0)

# Set up signal handling for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        match = re.search(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        
        if match:
            status_code = match.group(2)
            file_size = int(match.group(3))

            if status_code in valid_codes:
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

            total_size += file_size

        if line_count % 10 == 0:
            print_stats()

except Exception:
    pass
finally:
    print_stats()

