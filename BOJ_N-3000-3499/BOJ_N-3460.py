def main():
    T = int(input())
    for _ in range(T):
        n = bin(int(input()))[2:]
        for i in range(len(n) - 1, -1, -1):
            if n[i] == '1':
                print(len(n) - i - 1, end=' ')


if __name__ == "__main__":
    main()
