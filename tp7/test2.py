import unittest
from tp7 import Fraction


class TestFraction(unittest.TestCase):

    def test_init(self):

        frac1 = Fraction(3, 4)
        self.assertEqual(frac1._num, 3, "Test init : numérateur correct")
        self.assertEqual(frac1._den, 4, "Test init : dénominateur correct")


        frac2 = Fraction(6, 8)
        self.assertEqual(frac2._num, 3, "Test init : réduction correcte du numérateur")
        self.assertEqual(frac2._den, 4, "Test init : réduction correcte du dénominateur")


        with self.assertRaises(ValueError):
            Fraction(1, 0)


    def test_add(self):

        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 3)
        result = frac1 + frac2
        self.assertEqual(str(result), "5/6", "Test addition : somme correcte")

    def test_sub(self):

        frac1 = Fraction(5, 6)
        frac2 = Fraction(1, 3)
        result = frac1 - frac2
        self.assertEqual(str(result), "1/2", "Test soustraction : différence correcte")

    def test_mul(self):

        frac1 = Fraction(2, 3)
        frac2 = Fraction(3, 4)
        result = frac1 * frac2
        self.assertEqual(str(result), "1/2", "Test multiplication : produit correct")

    def test_div(self):

        frac1 = Fraction(2, 3)
        frac2 = Fraction(3, 4)
        result = frac1 / frac2
        self.assertEqual(str(result), "8/9", "Test division : quotient correct")


        frac3 = Fraction(0, 1)
        with self.assertRaises(ZeroDivisionError):
            frac1 / frac3

    def test_is_zero(self):

        frac1 = Fraction(0, 1)
        self.assertTrue(frac1.is_zero(), "Test is_zero : fraction égale à zéro")

        frac2 = Fraction(2, 3)
        self.assertFalse(frac2.is_zero(), "Test is_zero : fraction non nulle")

    def test_is_integer(self):

        frac1 = Fraction(4, 2)
        self.assertTrue(frac1.is_integer(), "Test is_integer : fraction entière")

        frac2 = Fraction(5, 2)
        self.assertFalse(frac2.is_integer(), "Test is_integer : fraction non entière")

    def test_as_mixed_number(self):


        frac2 = Fraction(1, 3)
        self.assertEqual(frac2.as_mixed_number(), "1/3", "Test as_mixed_number : fraction propre")


        frac3 = Fraction(7, 3)
        self.assertEqual(frac3.as_mixed_number(), "2 + 1/3", "Test as_mixed_number : fraction impropre")

    def test_is_proper(self):


        frac2 = Fraction(5, 4)
        self.assertFalse(frac2.is_proper(), "Test is_proper : fraction non propre")

    def test_is_unit(self):

        frac2 = Fraction(2, 1)
        self.assertFalse(frac2.is_unit(), "Test is_unit : fraction non unitaire")

    def test_is_adjacent_to(self):
        # Test si deux fractions sont adjacentes
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        self.assertTrue(frac1.is_adjacent_to(frac2), "Test is_adjacent_to : fractions adjacentes")

       

if __name__ == "__main__":
    unittest.main()
