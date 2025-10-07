def main():
    S = int(input())
    D = float(input())
    T = float(input())

    print("MADE IT" if S * 5_280 / 3_600 * T >= D else "FAILED TEST")


if __name__ == "__main__":
    main()
