def main():
    x, y = map(float, input().split())
    N = int(input())
    for _ in range(N):
        z, q = map(lambda e: e if e.isalpha() else float(e), input().split())
        k = (y / x) if q == "A" else (x / y)
        print(z * k)


if __name__ == "__main__":
    main()
