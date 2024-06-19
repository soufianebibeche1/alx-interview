# 0x08. Making Change

## Project Overview

This project focuses on the "coin change problem," a well-known problem in algorithm design. Your task is to find the minimum number of coins required to make up a specific total amount using a given set of coin denominations. This project will help you practice and apply your knowledge of greedy algorithms and dynamic programming.

## Learning Objectives

By completing this project, you should be able to:

1. **Understand and Implement Greedy Algorithms**:
   - Learn how greedy algorithms work and why they might be suitable for the coin change problem.
   - Identify cases where greedy algorithms do not yield the optimal solution.

2. **Master Dynamic Programming (DP)**:
   - Apply dynamic programming techniques to solve the coin change problem.
   - Understand the concepts of overlapping subproblems and optimal substructure.
   - Explore both iterative and recursive approaches to dynamic programming.

3. **Analyze Algorithmic Complexity**:
   - Assess the time and space complexity of different algorithms.
   - Strive for solutions with lower complexity to meet performance constraints.

4. **Develop Problem-Solving Strategies**:
   - Break down complex problems into smaller, manageable sub-problems.
   - Use Python effectively to implement solutions, including control flow tools and list manipulations.

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS, Python 3.4.3
- **File Conventions**:
  - All files must end with a new line.
  - The first line of each file must be `#!/usr/bin/python3`.
  - Use the `.py` extension for all Python files.
  - Follow PEP 8 style guide (version 1.7.x).
  - Ensure all files are executable.

## Concepts and Resources

### Key Concepts

1. **Greedy Algorithms**:
   - Greedy algorithms build a solution piece by piece, always choosing the next piece that offers the most immediate benefit.
   - They are simple and often provide the optimal solution for the coin change problem when the coin denominations have specific properties.

2. **Dynamic Programming**:
   - Dynamic programming solves problems by breaking them down into simpler sub-problems and storing the results of these sub-problems to avoid redundant calculations.
   - It is particularly useful for the coin change problem, providing a systematic approach to finding the minimum number of coins.

3. **Algorithmic Complexity**:
   - Analyze the efficiency of your algorithm in terms of time and space complexity.
   - Dynamic programming often offers a more efficient solution than greedy algorithms for the coin change problem.

4. **Problem-Solving Strategies**:
   - Approach the problem methodically by dividing it into smaller, solvable components.
   - Use iterative or recursive methods to implement dynamic programming solutions.

### Resources

- **Python Official Documentation**:
  - [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)

- **GeeksforGeeks Articles**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

- **YouTube Tutorials**:
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=1R0_7HqNaW0)

## Implementation Guide

### Greedy Algorithm Example
