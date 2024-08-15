#!/usr/bin/python3
import sys
import re
import signal

total_size = 0
status_codes = {}

def print_stats():
    """Prints the current log statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """Handles Ctrl+C to print stats and exit gracefully."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        try:
            match = re.match(r'.*?\s-\s.*?\s\[.*?\]\s"(GET|POST|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE|PATCH)\s\/projects\/260\sHTTP\/1.1"\s([2-5][0-9][0-9])\s(\d+)', line)
            if match:
                status_code = int(match.group(2))
                file_size = int(match.group(3))

                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

                if line_count % 10 == 0:
                    print_stats()

        except Exception:
            pass

    print_stats() 
