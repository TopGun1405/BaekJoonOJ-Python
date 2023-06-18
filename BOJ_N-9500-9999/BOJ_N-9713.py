def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        n = 0
        for i in range(1, N + 1, 2):
            n += i
        print(n)


if __name__ == "__main__":
    main()
