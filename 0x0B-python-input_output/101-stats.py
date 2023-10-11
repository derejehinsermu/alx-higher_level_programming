#!/usr/bin/python3
"""This module defines a script that reads stdin line by line and computes metrics."""

import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {}
line_count = 0

def print_metrics():
    """Print metrics based on the accumulated data."""
    print("Total file size:", total_file_size)

    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")

def process_line(line):
    """Process a line and update metrics."""
    global total_file_size
    global line_count

    line_count += 1

    if line_count % 10 == 0:
        print_metrics()

    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        file_size = parts[-1]

        # Update total file size
        total_file_size += int(file_size)

        # Update status code counts
        if status_code in ['200', '301', '400', '401', '403', '404', '405', '500']:
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

try:
    for line in sys.stdin:
        process_line(line.strip())

except KeyboardInterrupt:
    print_metrics()