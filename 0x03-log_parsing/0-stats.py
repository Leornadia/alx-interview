#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_file_size = 0
status_code_counts = {
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

# Regular expression to match the input format
log_pattern = re.compile(
    r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

# Function to print statistics
def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

# Signal handler for CTRL + C
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Set up signal handling
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))

            # Update total file size
            total_file_size += file_size

            # Update status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()

except Exception as e:
    pass

finally:
    # Print the final stats when the loop ends
    print_stats()

