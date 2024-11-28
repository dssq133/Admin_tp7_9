from tp7 import Fraction

def main():
    try:
        # Création de fractions
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(5, 1)
        f4 = Fraction(-2, 3)

        print("Fraction 1 :", f1)
        print("Fraction 2 :", f2)
        print("Fraction 3 :", f3)
        print("Fraction 4 :", f4)


        print("\nReprésentation en nombre mixte de f1 :", f1.as_mixed_number())
        print("Représentation en nombre mixte de f4 :", f4.as_mixed_number())


        print("\nAddition :", f1, "+", f2, "=", f1 + f2)
        print("Soustraction :", f1, "-", f2, "=", f1 - f2)
        print("Multiplication :", f1, "*", f2, "=", f1 * f2)
        print("Division :", f1, "/", f2, "=", f1 / f2)
        print("Égalité :", f1, "==", Fraction(2, 4), "?", f1 == Fraction(2, 4))


        print("\nEst nulle ?", f1, ":", f1.is_zero())
        print("Est un entier ?", f3, ":", f3.is_integer())
        print("Est propre ?", f4, ":", f4.is_proper())
        print("Est unitaire ?", f1, ":", f1.is_unit())
        print("Est adjacente à ?", f1, "et", Fraction(1, 3), ":", f1.is_adjacent_to(Fraction(1, 3)))


        print("\nValeur décimale de f1 :", float(f1))


        print("\nTest avec un dénominateur de zéro :")
        f_invalid = Fraction(1, 0)

    except ValueError as e:
        print("Erreur de valeur :", e)

    except ZeroDivisionError as e:
        print("Erreur de division :", e)

    except TypeError as e:
        print("Erreur de type :", e)

    except Exception as e:
        print("Autre erreur :", e)

if __name__ == "__main__":
    main()
