def main():
    X = int(input())
    N = int(input())
    tot = 0
    for _ in range(N):
        a, b = map(int, input().split())
        tot = tot + a * b
    print("Yes" if tot == X else "No")


if __name__ == "__main__":
    main()
