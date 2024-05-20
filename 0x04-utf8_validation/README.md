# 0x04. UTF-8 Validation

## Description

This project involves creating a Python script to validate whether a given dataset represents valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication. The goal is to ensure that a series of integers can be interpreted as a valid UTF-8 sequence.

## Concepts

To successfully complete this project, you will need to understand and apply the following concepts:

- **Bitwise Operations in Python**: Learn to manipulate bits using AND (&), OR (|), XOR (^), NOT (~), and bit shifts (<<, >>).
- **UTF-8 Encoding Scheme**: Familiarize yourself with UTF-8 encoding rules, including patterns for valid UTF-8 characters.
- **Data Representation**: Work with data at the byte level and handle the least significant bits of integers.
- **List Manipulation in Python**: Iterate through lists, access elements, and use list comprehensions.
- **Boolean Logic**: Apply logical operations for decision-making within the program.

## Resources

- [Python Bitwise Operators](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)
- [UTF-8 Encoding](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
- [PEP 8 Style Guide](https://pep8.org/)

## Requirements

- **General**
  - Use allowed editors: `vi`, `vim`, `emacs`
  - Files interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
  - Files should end with a new line
  - First line of all files: `#!/usr/bin/python3`
  - Include a `README.md` file at the root of the project folder
  - Follow PEP 8 style (version 1.7.x)
  - All files must be executable

## Implementation

### Step 1: Understanding UTF-8 Encoding Rules

UTF-8 encoding uses the following byte patterns for different numbers of bytes:

- 1 byte: 0xxxxxxx
- 2 bytes: 110xxxxx 10xxxxxx
- 3 bytes: 1110xxxx 10xxxxxx 10xxxxxx
- 4 bytes: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

### Step 2: Bitwise Operations

Use bitwise operations to extract and validate bits according to the UTF-8 patterns.

### Step 3: Python Script

Create a Python script to validate the dataset. Ensure the script adheres to PEP 8 guidelines and is executable.

### Example Script Structure
