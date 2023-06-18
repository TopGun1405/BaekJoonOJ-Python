def main():
    n = int(input())
    v = list(map(int, input().split()))
    print(sum(v) - max(v))


if __name__ == "__main__":
    main()
