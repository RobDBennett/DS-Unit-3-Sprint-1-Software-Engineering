#!/usr/bin/env python

# Part 4 of the spring challenge. This file should generate a random product and print a summary.
from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    y = range(0, num_products)
    for _ in y:
        a = random.choice(ADJECTIVES)
        b = random.choice(NOUNS)
        c = ' '
        name = a + c + b
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        item = Product(name, price, weight, flammability)
        products.append(item)
    return products


def inventory_report(products):
    names = []
    prices = []
    weights = []
    flammabilities = []
    for _ in products:
        name = _.name
        price = _.price
        weight = _.weight
        flames = _.flammability
        names.append(name)
        prices.append(price)
        weights.append(weight)
        flammabilities.append(flames)
    return names, prices, weights, flammabilities


if __name__ == '__main__':
    names, prices, weights, flammabilities = inventory_report(
        generate_products())
    myset = set(names)
    print("***************************************************************************")
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:", len(myset))
    print("Average Price:", (sum(prices) / len(prices)))
    print("Average Weight:", (sum(weights) / len(weights)))
    print("Average flammability:", (sum(flammabilities) / len(flammabilities)))
    print("***************************************************************************")
