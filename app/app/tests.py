from django.test import TestCase

from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """ test that two numbers are added together """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Subtract x from y and return value"""
        self.assertEqual(subtract(89, 8), 81)
