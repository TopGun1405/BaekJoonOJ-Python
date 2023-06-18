def main():
    n = int(input())
    trash = list(map(int, input().split()))
    minI, minT = 0, 1e9
    for i, v in enumerate(trash):
        if v < minT:
            minI, minT = i, v
    print(minI)


if __name__ == "__main__":
    main()
