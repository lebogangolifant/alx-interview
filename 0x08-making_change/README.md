# 0x08. Making Change

## Overview

This project contains a Python script (`0-making_change.py`) that implements a function to determine the fewest number of coins needed to meet a given total amount using dynamic programming. Additionally, a test script (`0-main.py`) is provided to demonstrate the functionality of the implemented function.

## Files

- **0-making_change.py**: Contains the `makeChange` function that determines the fewest number of coins needed to meet a given total amount.
- **0-main.py**: A test script that imports and tests the `makeChange` function.

## Concepts Covered

- ~~**Dynamic Programming**: The script demonstrates the use of dynamic programming to solve the coin change problem efficiently by breaking it down into smaller subproblems.~~
- **Greedy Algorithm**: The optimized implementation of the `makeChange` function uses a greedy algorithm to efficiently determine the fewest number of coins needed.
- **Python Programming**: The implementation showcases basic Python programming concepts, including loops, conditionals, and lists.

## Efficiency Improvement

The initial implementation of the `makeChange` function used dynamic programming, which can be less efficient in some cases. To improve efficiency, the implementation was updated to use a greedy algorithm, resulting in faster execution time.

## Usage

To test the `makeChange` function:
- Make the script executable:
```bash
chmod u+x 0-main.py
```
- Run the provided test script:

```bash
./0-main.py
```

This will display the fewest number of coins needed to meet a given total amount for different sets of coins.
