from math import factorial


def main():
    print("n e")
    print("- -----------")
    print("0 1")
    print("1 2")
    print("2 2.5")
    print("3 2.666666667")
    print("4 2.708333333")
    for n in range(5, 10):
        print(n, f"{sum([1 / factorial(i) for i in range(n+1)]):.9f}")


if __name__ == "__main__":
    main()
