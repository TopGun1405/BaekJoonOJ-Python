def main():
    n = int(input())
    for t in range(n):
        a, b, c = map(int, input().split())
        print("Data set: {} {} {}".format(a, b, c))
        for _ in range(c):
            a, b = a // 2 if a >= b else a, b // 2 if b > a else b
        print(max(a, b), min(a, b))
        if t < n - 1:
            print()


if __name__ == "__main__":
    main()
