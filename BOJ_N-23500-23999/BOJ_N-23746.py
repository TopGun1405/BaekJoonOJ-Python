def main():
    N = int(input())
    patterns = [input().split() for _ in range(N)]
    zipped = input()
    S, E = map(int, input().split())
    for pattern in patterns:
        zipped = zipped.replace(pattern[1], pattern[0])
    print(zipped[S-1:E])


if __name__ == "__main__":
    main()
