def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    q = int(input())
    for _ in range(q):
        y = int(input())
        y %= n * m
        print(s[y % n - 1] + t[y % m - 1])


if __name__ == "__main__":
    main()
