def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(*sorted(a))


if __name__ == "__main__":
    main()
