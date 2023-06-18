def main():
    T = int(input())
    for _ in range(T):
        n, chk = map(int, input().split())
        b = 1 if bin(n)[2:].count('1') % 2 else 0
        print("Valid" if b == chk else "Corrupt")


if __name__ == "__main__":
    main()
