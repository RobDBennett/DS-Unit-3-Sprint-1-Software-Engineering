#!/usr/bin/env python

# The first part of the challenge- to build a Class for products.

import random


class Product:
    """A Class to produce Acme products.
    Parameters-
    :var name: str
    :var price: int
    :var weight: int
    :var flammability: float
    :var identifier: int- randomly assigned upon creation
    """

    def __init__(self, name: str, price=10, weight=20, flammability=.5):
        self.name = name
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """A method to determine how easy the product is to steal. A ratio of price and weight."""
        theft = self.price / self.weight
        if theft < .5:
            return "Not so stealable..."
        elif .5 <= theft < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """A method to illustrate the explosive properties of the product. A ratio of flammability and weight."""
        burn = self.flammability * self.weight
        if burn < 10:
            return "...fizzle."
        elif 10 <= burn < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """A child of the Product class.
    Parameters-
    :var name: str
    :var price: int
    :var weight: int
    :var flammability: float
    :var identifier: int- randomly assigned upon creation 
    """

    def __init__(self, name: str, price=10, weight=10, flammability=.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        """A method to replace the explode product method. Gloves aren't known to explode."""
        return "...it's a glove."

    def punch(self):
        """A new method to determine how much it will hurt to be punched by this product."""
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey, that hurt!"
        else:
            return "OUCH!"
