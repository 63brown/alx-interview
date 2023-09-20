#!/usr/bin/python3
"""
Log Parsing
"""

import sys
import re
from collections import defaultdict

# Regular expression to match the input format
pattern = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] '
    r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)')

# Initialize variables for metrics
total_size = 0
status_code_count = defaultdict(int)
lines_processed = 0

try:
    """reads stdin line by line and computes metrics"""
    for line in sys.stdin:
        # Match the input line with the regular expression
        match = pattern.match(line)
        if match:
            ip_address, date, status_code, file_size = match.groups()
            total_size += int(file_size)
            status_code = int(status_code)
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_code_count[status_code] += 1
            lines_processed += 1
            if lines_processed % 10 == 0:
                print(f"Total file size: File size: {total_size}")
                for code in sorted(status_code_count.keys()):
                    print(f"{code}: {status_code_count[code]}")
                print()
except KeyboardInterrupt:
    pass

print(f"Total file size: File size: {total_size}")
for code in sorted(status_code_count.keys()):
    print(f"{code}: {status_code_count[code]}")
