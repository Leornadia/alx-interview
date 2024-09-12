# 0x07. Rotate 2D Matrix

## Description
This project implements an in-place algorithm to rotate a 2D matrix by 90 degrees clockwise.

## Algorithm
The algorithm works by performing the following steps:

1. **Transpose the matrix:** Swap the elements across the main diagonal (top-left to bottom-right).
2. **Reverse each row:** Reverse the order of elements in each row.

## File: `0-rotate_2d_matrix.py`

This file contains the implementation of the `rotate_2d_matrix` function.

**Function Prototype:**
```python
def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix: A list of lists representing the 2D matrix.
    """
    # ... implementation ...

Example Usage:
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>> rotate_2d_matrix(matrix)
>>> print(matrix)
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]

Requirements
Python 3.8.10
pycodestyle 2.8.0
How to Use
Clone the repository:
git clone https://github.com/your-username/alx-interview.git

Navigate to the project directory:
cd 0x07-rotate_2d_matrix

Run the example:
python3 main_0.py

Author
Leornadia Jose 
