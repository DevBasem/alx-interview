#!/usr/bin/python3
"""Generate Pascal's Triangle up to the nth row."""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    
    Args:
    n (int): The number of rows in Pascal's Triangle.
    
    Returns:
    list of lists: The Pascal's Triangle up to the nth row.
    """
    # Edge case: Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate subsequent rows
    for i in range(1, n):
        # Each row starts and ends with 1
        row = [1]
        # Calculate the elements in between using the previous row
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)
        row.append(1)
        triangle.append(row)
    
    return triangle

# Test the function
if __name__ == "__main__":
    # Define a function to print the triangle
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))
    
    # Print Pascal's Triangle with 5 rows
    print_triangle(pascal_triangle(5))
