#!/usr/bin/python3

import sys
import signal

# Initialize variables
total_size = 0
status_codes = {
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

        # Split the line by space
        parts = line.split()

        if len(parts) < 7:
            continue  # Skip if the line does not have enough parts

        # Extract file size and status code
        file_size = parts[-1]
        status_code = parts[-2]

        # Validate and process file size
        try:
            total_size += int(file_size)
        except ValueError:
            continue  # Skip if the file size is not a valid integer

        # Validate and process status code
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    pass
finally:
    print_stats()

