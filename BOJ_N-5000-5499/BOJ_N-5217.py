def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        pair = [(i, n - i) for i in range(1, n // 2 + 1) if i < n - i]
        print("Pairs for {}: ".format(n), end='')
        for i in range(len(pair)):
            a, b = pair[i]
            if i == 0:
                print("{} {}".format(a, b), end='')
            else:
                print(", {} {}".format(a, b), end='')
        print()


if __name__ == "__main__":
    main()
