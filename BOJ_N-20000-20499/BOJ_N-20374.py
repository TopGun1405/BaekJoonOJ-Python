import sys


def main():
    moneys = sys.stdin.readlines()

    tot = 0
    for money in moneys:
        n1, n2 = map(int, money.split("."))

        tot += n1 * 100 + n2

    print(f"{tot // 100}.{tot % 100:02d}")


if __name__ == "__main__":
    main()
