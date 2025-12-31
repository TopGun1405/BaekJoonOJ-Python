def main():
    n = int(input())
    p = int(input())
    S = list(map(int, input().split()))

    print(*(set(range(p, p+n)) - set(S)))


if __name__ == "__main__":
    main()
