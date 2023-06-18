def main():
    N = int(input())
    choco = list(map(int, input().split()))
    box = 0
    for a, b in zip(choco[:-1], choco[1:]):
        if a < b:
            box += 1
    print(box)


if __name__ == "__main__":
    main()
