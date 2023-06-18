def main():
    T = int(input())
    for _ in range(T):
        k = int(input())
        p = 1
        for n in range(k - 1):
            p = 2 * p + 1
        print(p)


if __name__ == "__main__":
    main()
