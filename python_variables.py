# Python Variables

# Variable assignment
x = 5           # Integer variable
y = "Hello"     # String variable

# Print variables
print("x:", x)
print("y:", y)

# Changing the value of a variable
x = 10
print("New value of x:", x)

# Multiple variables in one line
a, b, c = 3, 4, 5
print("a:", a, "b:", b, "c:", c)

# Global and Local variables
def my_function():
    z = 20  # Local variable
    print("Inside function, z:", z)

my_function()
# Uncommenting the next line will cause an error because z is local to the function.
# print("Outside function, z:", z)

