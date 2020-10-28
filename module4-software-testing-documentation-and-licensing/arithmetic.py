#!/usr/bin/env python

# Create a class SimpleOperations which takes two arguements:
# 1. 'a' (an integer)
# 2. 'b' (an integer)

# Create methods for (a, b) which will:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide

# Create a child class Complex which will inherit from SimpleOperations
# and take (a, b) as arguements (same as the former class).

# Create methods for (a, b) which will perform:
# 1. Exponentiation ('a' to the power of 'b')
# 2. Nth Root ('b'th root of 'a')

# Make sure each class/method includes a docstring

# Make sure entire script conforms to PEP8 guidelines

# Check your work by running the script


class SimpleOperations:
    """A constructor for simple math.
    Parameters-
    :var a: int
    :var b: int
    """

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return f'Cannot divide by zero!'
        else:
            return self.a / self.b


class Complex(SimpleOperations):
    """A constructor for more complicated math.
    :var a: int
    :var b: int
    """

    def __init__(self, a, b) -> None:
        super().__init__(a, b)

    def exponentiation(self):
        return self.a ** self.b

    def nth_root(self):
        return round((self.a ** (1.0 / self.b)), 4)


if __name__ == "__main__":
    print(SimpleOperations(3, 2).add())
    print('-------------------')
    print(SimpleOperations(3, 2).subtract())
    print('-------------------')
    print(SimpleOperations(3, 2).multiply())
    print('-------------------')
    print(SimpleOperations(3, 2).divide())
    print('-------------------')
    print(Complex(3, 2).exponentiation())
    print('-------------------')
    print(Complex(3, 2).nth_root())
    print('-------------------')
