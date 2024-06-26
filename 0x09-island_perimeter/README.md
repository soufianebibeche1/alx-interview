# Island Perimeter

## Project Overview

The goal of this project is to calculate the perimeter of a single island within a grid. The grid is represented as a 2D list (matrix) of integers, where:
- `0` represents water.
- `1` represents land.

An island is a group of `1`s connected vertically or horizontally. The task is to determine the perimeter of this island by analyzing its surrounding cells.

## Key Concepts

### 2D Arrays (Matrices)
- Understanding how to access and iterate over elements in a 2D array is essential.
- You need to navigate through adjacent cells in the grid to determine the perimeter of the island.

### Conditional Logic
- Apply conditions to check if a cell is part of the perimeter.
- Identify if neighboring cells are water or out of the grid bounds.

### Counting Techniques
- Develop a method to count the edges that contribute to the island's perimeter.

### Problem-Solving Strategies
- Break down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- Each file should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the project is mandatory.
- Code must follow PEP 8 style (version 1.7).
- No external modules or imports are allowed.
- All modules and functions must be documented.
- All files must be executable.

## Implementation

### Steps
1. **Access Grid Cells**: Iterate through each cell in the 2D grid.
2. **Check Perimeter Conditions**: For each land cell (`1`), check its adjacent cells (up, down, left, right).
3. **Count Perimeter Edges**: Determine if an adjacent cell is water (`0`) or outside the grid, and count it towards the perimeter.

### Example
