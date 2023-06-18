def main():
    num = [int(input()) for _ in range(7)]
    ans = [n for n in num if n % 2 == 1]
    print("{}\n{}".format(sum(ans), min(ans)) if len(ans) > 0 else -1)


if __name__ == "__main__":
    main()
