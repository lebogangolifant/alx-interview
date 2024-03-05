# 0x09. Island Perimeter

## Overview

This project contains a Python script (`0-island_perimeter.py`) that implements a function to calculate the perimeter of an island represented by a 2D grid. Additionally, a test script (`0-main.py`) is provided to demonstrate the functionality of the implemented function.

## Files

- **0-island_perimeter.py**: Contains the `island_perimeter` function that calculates the perimeter of the island described in the input grid.
- **0-main.py**: A test script that imports and tests the `island_perimeter` function.

## Concepts Covered

- **2D Arrays (Matrices)**: The script demonstrates accessing and iterating over elements in a 2D array, along with navigating through adjacent cells (horizontally and vertically).
- **Conditional Logic**: The implementation applies conditions to determine whether a cell contributes to the perimeter of the island.
- **Python Programming**: The script uses nested loops for iterating over grid cells and conditional statements to check the status of adjacent cells.

## Usage

To test the `island_perimeter` function:
- Make the script executable:
```bash
chmod u+x 0-main.py
```
- Run the provided test script:

```bash
./0-main.py
```

This will display the perimeter of the island for a given 2D grid representing land and water.
