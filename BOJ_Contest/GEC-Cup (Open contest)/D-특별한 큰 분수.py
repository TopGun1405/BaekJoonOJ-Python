def main():
    x0, N = map(int, input().split())
    temp = x0
    print((2 * temp) ^ 6)
    print(temp ^ 5)
    print((temp // 2) ^ 4)
    print()
    print((((temp // 2) ^ 4) // 2) ^ 6)
    print()
    for _ in range(N):
        x0 = (2 * x0) ^ 6 if x0 % 2 else (x0 // 2) ^ 6
        print(x0)
    print(x0)


if __name__ == "__main__":
    main()
