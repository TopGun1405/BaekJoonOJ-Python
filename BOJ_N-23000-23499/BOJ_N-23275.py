def main():
    n = int(input())
    x = set(map(int, input().split()))
    y = set(map(int, input().split()))
    print(*(x - y))


if __name__ == "__main__":
    main()
