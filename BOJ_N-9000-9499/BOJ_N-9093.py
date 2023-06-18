def main():
    T = int(input())
    for _ in range(T):
        text = list(map(lambda s: s[::-1], input().split()))
        print(' '.join(text))


if __name__ == "__main__":
    main()
