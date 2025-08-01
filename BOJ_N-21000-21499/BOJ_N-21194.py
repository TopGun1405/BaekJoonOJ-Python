def main():
    n, k = map(int, input().split())
    score = sorted([int(input()) for _ in range(n)])

    print(sum(score[-k:]))


if __name__ == "__main__":
    main()
