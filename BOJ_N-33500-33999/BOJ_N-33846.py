def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    print(*(sorted(a[:t]) + a[t:]))


if __name__ == "__main__":
    main()
