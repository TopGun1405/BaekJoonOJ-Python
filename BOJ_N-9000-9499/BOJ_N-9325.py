def main():
    t = int(input())
    for _ in range(t):
        s = int(input())
        n = int(input())
        for _ in range(n):
            q, p = map(int, input().split())
            s += p * q
        print(s)


if __name__ == "__main__":
    main()
