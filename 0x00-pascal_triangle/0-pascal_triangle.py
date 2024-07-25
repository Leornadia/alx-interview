def pascal_triangle(n):
    """Returns a list of lists representing Pascal's Triangle of n rows."""
    
    # Step 1: Check for edge case
    if n <= 0:
        return []
    
    # Step 2: Initialize the triangle with the first row
    triangle = [[1]]  # The first row of Pascal's Triangle

    # Step 3: Build the triangle row by row
    for i in range(1, n):
        row = [1]  # Start with 1
        last_row = triangle[-1]  # Get the last row
        
        # Fill in the values in between
        for j in range(1, i):
            # The value is the sum of the two values above it
            value = last_row[j - 1] + last_row[j]
            row.append(value)
        
        row.append(1)  # End with 1
        triangle.append(row)  # Add the completed row to the triangle
    
    # Step 4: Return the complete triangle
    return triangle

# This is how you would use the function in practice.
if __name__ == "__main__":
    # Example usage of the function and printing the triangle
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)  # Print each row of Pascal's Triangle
