#!/usr/bin/python3
"""
Reads input from stdin line by line and computes metrics"""
import sys

file_size = 0
status_counts = {"200": 0, "301": 0, "400": 0, "401": 0,
                        "403": 0, "404": 0, "405": 0, "500": 0}
c = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            a = c
            if tokens[-2] in status_counts:
                status_counts[tokens[-2]] += 1
                c += 1
            try:
                file_size += int(tokens[-1])
                if a == c:
                    c += 1
            except FileNotFoundError:
                if a == c:
                    continue
        if c % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_counts.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_counts.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_counts.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
