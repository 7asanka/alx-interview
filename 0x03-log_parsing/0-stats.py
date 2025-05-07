#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""


import sys
import signal


# Initialize counters
total_size = 0
status_counts = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0


def print_stats():
    """Print accumulated metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) < 7:
            continue

        # Extract status code and file size from the end
        status_code = parts[-2]
        file_size = parts[-1]

        try:
            total_size += int(file_size)
        except ValueError:
            continue

        if status_code in valid_codes:
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Final stats if script ends without interruption
print_stats()
