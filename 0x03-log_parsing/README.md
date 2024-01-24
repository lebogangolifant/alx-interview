# 0x03. Log Parsing

## Overview

This project consists of two Python scripts - `0-generator.py` and `0-stats.py` - designed for log parsing. The `0-generator.py` script generates log entries with random data, while the `0-stats.py` script reads the log entries from stdin, calculates metrics, and prints statistics after every 10 lines or upon receiving a keyboard interruption (CTRL + C).

## Files

- **0-generator.py**: Generates random log entries with IP addresses, dates, HTTP requests, status codes, and file sizes.
- **0-stats.py**: Parses log entries, calculates metrics, and prints statistics based on file sizes and HTTP status codes.

## Concepts Covered

- **Log Parsing**: The `0-stats.py` script demonstrates basic log parsing techniques, extracting relevant information such as IP addresses, dates, HTTP requests, status codes, and file sizes.

- **Exception Handling**: The script handles keyboard interruptions (Ctrl+C) gracefully to print final statistics before exiting.

- **Python Scripting**: Both scripts showcase fundamental Python scripting concepts, including file input/output, string manipulation, and dictionary usage.

## Usage

To generate random log entries and calculate statistics:
1. Make the generator script executable:

    ```bash
    chmod u+x 0-generator.py
    ```

2. Run the generator script and pipe the output to the statistics script:

    ```bash
    ./0-generator.py | ./0-stats.py
    ```

3. To stop the script use:
  ```bash
  (Ctrl+C)
  ```
(Ctrl+C) handles KeyboardInterrupt and print final statistics before exiting.  

This will display statistics based on file sizes and HTTP status codes after every 10 lines or upon keyboard interruption.

