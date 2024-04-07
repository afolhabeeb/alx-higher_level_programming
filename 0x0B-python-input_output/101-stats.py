#!/usr/bin/env python3

import sys

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    # Read lines from stdin
    for line_number, line in enumerate(sys.stdin, start=1):
        # Parse each line according to the input format
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update total file size
        total_file_size += file_size

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_number % 10 == 0:
            print(f"File size: {total_file_size}")
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    # Handle KeyboardInterrupt (Ctrl+C)
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
