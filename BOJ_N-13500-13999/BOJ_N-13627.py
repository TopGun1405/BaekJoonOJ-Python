def main():
    N, R = map(int, input().split())
    returned = set(map(int, input().split()))

    volunteers = set(range(1, N+1))
    missing = sorted(volunteers - returned)

    if not missing:
        print("*")
    else:
        print(*missing)


if __name__ == "__main__":
    main()
