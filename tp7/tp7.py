from math import gcd

class Fraction:
    """Class representing a fraction and operations on it.

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """Builds a fraction based on a numerator and a denominator.

        PRÉ : Le dénominateur (den) doit être différent de zéro.
        POST : La fraction est stockée sous sa forme réduite avec un dénominateur positif.
        """
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro.")
        div_commun = gcd(num, den)
        self._num = num // div_commun
        self._den = den // div_commun
        if self._den < 0:
            self._num = -self._num
            self._den = -self._den

    @property
    def numerator(self):
        return self._num

    @property
    def denominator(self):
        return self._den

    # ------------------ Textual Representations ------------------

    def __str__(self):
        """Returns a textual representation of the reduced form of the fraction.

        PRÉ : -
        POST : Retourne une chaîne au format "num/den" ou "num" si le dénominateur est 1.
        """
        if self._den == 1:
            return str(self._num)
        return f"{self._num}/{self._den}"

    def as_mixed_number(self):
        """Returns a textual representation of the fraction as a mixed number.

        A mixed number is the sum of an integer and a proper fraction.

        PRÉ : -
        POST : Retourne une chaîne au format "partie entière + (num/den)" si applicable.
        """
        partie_entiere = self._num // self._den
        reste = abs(self._num) % self._den
        if reste == 0:
            return str(partie_entiere)
        if partie_entiere == 0:
            return f"{reste}/{self._den}"
        return f"{partie_entiere} + {reste}/{self._den}"

    # ------------------ Operators Overloading ------------------

    def __add__(self, other):
        """Overloads the + operator for fractions.

        PRÉ : L'opérande doit être une instance de Fraction.
        POST : Retourne une nouvelle Fraction représentant la somme.
        """
        if isinstance(other, Fraction):
            new_num = self._num * other._den + other._num * self._den
            new_den = self._den * other._den
            return Fraction(new_num, new_den)
        raise TypeError("L'opérande doit être une Fraction.")

    def __sub__(self, other):
        """Overloads the - operator for fractions.

        PRÉ : L'opérande doit être une instance de Fraction.
        POST : Retourne une nouvelle Fraction représentant la différence.
        """
        if isinstance(other, Fraction):
            new_num = self._num * other._den - other._num * self._den
            new_den = self._den * other._den
            return Fraction(new_num, new_den)
        raise TypeError("L'opérande doit être une Fraction.")

    def __mul__(self, other):
        """Overloads the * operator for fractions.

        PRÉ : L'opérande doit être une instance de Fraction.
        POST : Retourne une nouvelle Fraction représentant le produit.
        """
        if isinstance(other, Fraction):
            new_num = self._num * other._num
            new_den = self._den * other._den
            return Fraction(new_num, new_den)
        raise TypeError("L'opérande doit être une Fraction.")

    def __truediv__(self, other):
        """Overloads the / operator for fractions and integers.

        Allows division by another Fraction or an integer.
        """
        if isinstance(other, Fraction):
            if other._num == 0:
                raise ZeroDivisionError("Impossible de diviser par une fraction avec un numérateur égal à 0.")
            new_num = self._num * other._den
            new_den = self._den * other._num
            return Fraction(new_num, new_den)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Fraction(self._num, self._den * other)
        raise TypeError("L'opérande doit être une Fraction ou un entier.")

    def __eq__(self, other):
        """Overloads the == operator for fractions.

        PRÉ : L'opérande doit être une instance de Fraction.
        POST : Retourne True si les fractions sont égales, sinon False.
        """
        return isinstance(other, Fraction) and \
               self._num == other._num and self._den == other._den

    def __float__(self):
        """Returns the decimal value of the fraction.

        PRÉ : -
        POST : Retourne un float représentant la fraction.
        """
        return self._num / self._den

    # ------------------ Properties Checking ------------------

    def is_zero(self):
        """Check if the fraction's value is 0.

        PRÉ : -
        POST : Retourne True si la fraction est nulle, sinon False.
        """
        return self._num == 0

    def is_integer(self):
        """Check if the fraction is an integer (e.g., 8/4, 3, 2/2, ...).

        PRÉ : -
        POST : Retourne True si la fraction est un entier, sinon False.
        """
        return self._num % self._den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1.

        PRÉ : -
        POST : Retourne True si la fraction est propre, sinon False.
        """
        return abs(self._num) < self._den

    def is_unit(self):
        """Check if the numerator of the fraction is equal to 1 in its reduced form.

        PRÉ : -
        POST : Retourne True si la fraction est unitaire, sinon False.
        """
        return abs(self._num) == 1 and self._den == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction.

        Two fractions are adjacent if the absolute value of the difference is a unit fraction.

        PRÉ : L'opérande doit être une instance de Fraction.
        POST : Retourne True si les fractions sont adjacentes, sinon False.
        """
        if isinstance(other, Fraction):
            diff = abs(self._num * other._den - other._num * self._den)
            den = self._den * other._den
            return diff == 1 and den > 0
        raise TypeError("L'opérande doit être une Fraction.")
