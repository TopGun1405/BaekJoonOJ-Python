def main():
    N = int(input())
    a = list(map(int, input().split()))
    lemon = 0
    for i, ai in enumerate(a):
        lemon = max(lemon, ai - (N - i))
    print(lemon)


if __name__ == "__main__":
    main()
