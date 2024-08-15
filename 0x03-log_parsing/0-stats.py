#!/usr/bin/python3

import sys

def print_statistics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_log_entry(line):
    parts = line.split()
    if len(parts) != 9:
        return None
    ip_address = parts[0]
    status_code = parts[8]
    file_size = parts[7]
    if not status_code.isdigit():
        return None
    return ip_address, status_code, file_size

def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            entry = parse_log_entry(line.strip())
            if entry is None:
                continue
            ip_address, status_code, file_size = entry
            total_size += int(file_size)
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if i % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        pass

    print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()
