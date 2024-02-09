# 0x05. N Queens

## Overview

This project contains a Python script (`0-nqueens.py`) that implements a solution to the N-Queens problem. Additionally, the script validates user input and prints every possible solution to the problem.

## Files

- **0-nqueens.py**: Contains functions to solve the N-Queens problem and validate user input.

## Concepts Covered

- **N-Queens Problem**: The script addresses the classic problem of placing N non-attacking queens on an N×N chessboard.
  
- **Backtracking Algorithm**: The implementation utilizes a backtracking algorithm to explore and find all possible solutions.

- **Command-Line Arguments**: The script parses command-line arguments to accept user input for the size of the chessboard.

## Usage

To solve the N-Queens problem and print solutions:
- Make the script executable:
```bash
chmod u+x 0-nqueens.py
```
- Run the script with the desired size of the chessboard (N):

```bash
./0-nqueens.py 4
```

```bash
./0-nqueens.py 6
```

This will execute the script and print every possible solution to the N-Queens problem for the specified chessboard size.
```
