def main():
    n = int(input())
    c = list(map(int, input().split()))
    print(sum(c) - max(c))


if __name__ == "__main__":
    main()
