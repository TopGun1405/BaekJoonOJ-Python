def main():
    x0, N = map(int, input().split())
    for _ in range(N):
        x0 = (2 * x0) ^ 6 if x0 % 2 else (x0 // 2) ^ 6
    print(x0)


if __name__ == "__main__":
    main()
