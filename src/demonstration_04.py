"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
def find_perimeter(length, width):
    l = length * 2
    w = width * 2
    return l + w

print(find_perimeter(6, 7))
print(find_perimeter(20, 10))
print(find_perimeter(2, 9))
