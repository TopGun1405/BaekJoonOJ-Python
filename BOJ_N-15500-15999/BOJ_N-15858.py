from decimal import Decimal


def main():
    a, b, c = map(int, input().split())
    result = Decimal(a) * Decimal(b) / Decimal(c)
    print(f"{result:.6f}")


if __name__ == "__main__":
    main()
