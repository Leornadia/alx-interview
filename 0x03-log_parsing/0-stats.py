#!/usr/bin/python3
import sys
import re
from collections import defaultdict

def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print(f"{status_code}: {status_codes[status_code]}")

def parse_logs():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0
    
    log_format = r'^(\S+) - \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(log_format, line)
            
            if match:
                status_code = int(match.group(3))
                file_size = int(match.group(4))
                
                total_size += file_size
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_codes[status_code] += 1
                line_count += 1
                
                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)
    
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise

if __name__ == "__main__":
    parse_logs()
