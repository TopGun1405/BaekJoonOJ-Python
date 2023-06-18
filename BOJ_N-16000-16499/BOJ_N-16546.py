def main():
    N = int(input())
    runners = set(map(int, input().split()))
    aR = set(range(1, N + 1))
    print(*(aR - runners))


if __name__ == "__main__":
    main()
