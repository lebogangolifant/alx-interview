# 0x04. UTF-8 Validation

## Overview

This project contains a Python script (`0-validate_utf8.py`) that implements a function to determine if a given data set represents a valid UTF-8 encoding. Additionally, a test script (`0-main.py`) is provided to demonstrate the functionality of the implemented function.

## Files

- **0-validate_utf8.py**: Contains the `validUTF8` function that checks the validity of a UTF-8 encoding.
- **0-main.py**: A test script that imports and tests the `validUTF8` function.

## Concepts Covered

- **UTF-8 Encoding**: The script handles the UTF-8 encoding, a variable-width character encoding that represents characters using 1 to 4 bytes.
  
- **Binary Manipulation**: The implementation involves bitwise operations and binary manipulation to validate the UTF-8 encoding.

- **Python Programming**: The script adheres to Python programming conventions, including loops, conditionals, and bitwise operations.

## Usage

To test the `validUTF8` function:
- Make the script executable:
```bash
chmod u+x 0-main.py
```
- Run the provided test script:

```bash
./0-main.py
```

This will execute the test cases and display whether the given data sets represent valid UTF-8 encodings.
