#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    """
    Print the statistics based on the total file size
    and the number of lines for each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                    "404": 0, "405": 0, "500": 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()

            # Check if the line has the expected format
            if len(parts) >= 7:
                status_code = parts[-2]
                file_size = int(parts[-1])

                # Check if the status code is valid
                if status_code in status_codes:
                    total_size += file_size
                    status_codes[status_code] += 1

            # Print statistics after every 10 lines
            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
