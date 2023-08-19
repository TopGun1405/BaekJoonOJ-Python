from fractions import Fraction
from decimal import Decimal


def withModule(m: int):
    try:
        n = Fraction(Decimal(m))
        print("YES")
        print(n.numerator, n.denominator)
    except Exception:
        print("NO")


def main():
    k = input()
    try:
        n = Fraction(Decimal(k))
        print("YES")
        print(n.numerator, n.denominator)
    except Exception:
        print("NO")


if __name__ == "__main__":
    main()
