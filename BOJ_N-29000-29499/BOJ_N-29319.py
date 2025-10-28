def main():
    n = int(input())
    a = list(map(int, input().split()))

    print(sum(sorted(a)[:-1]))


if __name__ == "__main__":
    main()
