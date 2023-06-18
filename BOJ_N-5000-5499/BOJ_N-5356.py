def main():
    T = int(input())
    for _ in range(T):
        N, C = input().split()
        for i in range(int(N)):
            print(chr((ord(C) + i - 65) % 26 + 65) * (i + 1))
        if _ < T - 1:
            print()


if __name__ == "__main__":
    main()
