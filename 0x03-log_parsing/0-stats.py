#!/usr/bin/python3
import re
import signal
import sys

# Signal handler for keyboard interruption (CTRL + C)
def handler(signal_received, frame):
    print_metrics()
    sys.exit(0)

# Dictionary to store status code counts
status_codes = {}

# Total file size
total_size = 0

# Line count
line_count = 0

# Regular expression pattern to match log entry format
pattern = r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'

# Register signal handler
signal.signal(signal.SIGINT, handler)

def print_metrics():
    print(f"File size: {total_size}")
    
    # Sort status codes in ascending order
    sorted_codes = sorted(status_codes.items(), key=lambda x: x[0])
    
    for code, count in sorted_codes:
        print(f"{code}: {count}")

try:
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        
        match = re.match(pattern, line)
        if match:
            ip, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)
            
            # Update status code counts
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
            
            # Update total file size
            total_size += file_size
            
            # Increment line count
            line_count += 1
            
            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics()
        
except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
