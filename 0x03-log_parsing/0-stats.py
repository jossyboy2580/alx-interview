#!/usr/bin/python3
"""
A Log parser

This module contains a log parsing script that takes in logs as an input and
extracts some key metrics from it

Format of the log

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""
import sys
import re


def main(logs):
    """
    The main program that interpret the logs
    """

    regex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - ' \
            r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] ' \
            r'"GET /projects/260 HTTP/1\.1" (?P<code>\d{3}) (?P<length>\d+)$'

    code_count = {}
    total_size = 0
    for log in logs:
        match = re.match(regex, log)

        code = match.groupdict()['code']
        size = match.groupdict()['length']

        code_count[code] = code_count.get(code, 0) + 1
        total_size += int(size)
    print(f'File size: {total_size}')
    for key in sorted(code_count.keys()):
        print(f'{key}: {code_count[key]}')


if __name__ == "__main__":

    #  Read the logs from the piped in input into a list
    # logs = sys.stdin.readlines()
    while True:
        logs = []
        for i in range(10):
            logs.append(sys.stdin.readline())
        main(logs)

    # main(logs)
