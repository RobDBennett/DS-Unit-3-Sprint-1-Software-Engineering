#!/usr/bin/env python

import unittest
import random
from acme import Product, BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS, inventory_report


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_explode(self):
        """Test to see if the product explodes as it should."""
        prod = Product('Test Product', 10, 50, 2.5)
        explode = prod.explode()
        self.assertEqual(explode, "...BABOOM!!")

    def test_theft(self):
        """Test to see if the product is easy to steal or not."""
        prod = Product('Test Product', 10, 50, 2.5)
        steal = prod.stealability()
        self.assertEqual(steal, "Not so stealable...")

    def test_punch(self):
        """A test to see if the product carries the right 'punch'."""
        prod = BoxingGlove('TestPunch', 10, 50, 2.5)
        punch = prod.punch()
        self.assertEqual(punch, "OUCH!")


class AcmeReportTests(unittest.TestCase):
    """Making sure that Acme is reporting accurately."""

    def test_default_num_products(self):
        """Test to ensure that the default lists are acting appropraitely"""
        prods = generate_products()
        self.assertEqual(len(prods), 30)

    def test_legal_names(self):
        """A test to ensure that the names generated in our report are 'legal'.
        They should be Adjective Space Noun. I've ran my own instance tests, and I
        know that they are indeed generated along those lines, but this test confirms.
        """
        names, prices, weights, flammabilities = inventory_report(
            generate_products(1))
        possible_names = []
        for _ in range(0, 100):
            a = random.choice(ADJECTIVES)
            b = random.choice(NOUNS)
            c = ' '
            unique = a + c + b
            possible_names.append(unique)
        res = any(ele in names for ele in possible_names)
        self.assertTrue(res)

    def test_inventory_reporting(self):
        """A test to ensure that we are running the proper number of items in our reports."""
        names, prices, weights, flammabilities = inventory_report(
            generate_products(50))
        self.assertEqual(len(names), 50)


if __name__ == '__main__':
    unittest.main()
